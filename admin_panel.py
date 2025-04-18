from config import Config, Txt
from helper.database import codeflixbots, weooanimes
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import os, sys, time, asyncio, logging, datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure ADMIN is an integer or list of integers
ADMIN_USER_ID = int(Config.ADMIN) if isinstance(Config.ADMIN, str) else Config.ADMIN

# Flag to indicate if the bot is restarting
is_restarting = False

@Client.on_message(filters.private & filters.command("restart") & filters.user(ADMIN_USER_ID))
async def restart_bot(b, m):
    global is_restarting
    if not is_restarting:
        is_restarting = True
        await m.reply_text("**Restarting... Please wait.**")

        # Gracefully stop the bot's event loop
        b.stop()
        time.sleep(2)  # Small delay to allow graceful shutdown

        # Restart the bot process
        os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.private & filters.command("tutorial"))
async def tutorial(bot: Client, message: Message):
    user_id = message.from_user.id
    format_template = await codeflixbots.get_format_template(user_id) or "No format set."
    await message.reply_text(
        text=Txt.FILE_NAME_TXT.format(format_template=format_template),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("• ᴏᴡɴᴇʀ", url="https://t.me/otakukart7"),
                InlineKeyboardButton("• ᴛᴜᴛᴏʀɪᴀʟ", url="https://t.me/weoo_anime")
            ]
        ])
    )


@Client.on_message(filters.command(["stats", "status"]) & filters.user(ADMIN_USER_ID))
async def get_stats(bot, message):
    total_users = await weooanimes.total_users_count()
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - getattr(bot, "uptime", time.time())))
    start_t = time.time()
    st = await message.reply('**Accessing The Details...**')
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await st.edit(
        text=(
            f"**-- Bot Status --**\n\n"
            f"**⌚ Uptime:** `{uptime}`\n"
            f"**🐌 Ping:** `{time_taken_s:.3f} ms`\n"
            f"**👭 Total Users:** `{total_users}`"
        )
    )


@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_USER_ID) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    await bot.send_message(Config.LOG_CHANNEL, f"{m.from_user.mention} ({m.from_user.id}) started a broadcast.")
    all_users = await codeflixbots.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Broadcast Started...")
    
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = await weooanimes.total_users_count()

    async for user in all_users:
        sts = await send_msg(user['_id'], broadcast_msg)
        if sts == 200:
            success += 1
        else:
            failed += 1
        if sts == 400:
            await weooanimes.delete_user(user['_id'])
        done += 1

        if not done % 20:
            await sts_msg.edit(
                f"Broadcast in progress:\n\n"
                f"Total Users: {total_users}\n"
                f"Completed: {done} / {total_users}\n"
                f"✅ Success: {success}\n"
                f"❌ Failed: {failed}"
            )

    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(
        f"**Broadcast Completed!**\n\n"
        f"Duration: `{completed_in}`\n"
        f"Total Users: `{total_users}`\n"
        f"✅ Success: `{success}`\n"
        f"❌ Failed: `{failed}`"
    )


async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(user_id, message)
    except (InputUserDeactivated, UserIsBlocked, PeerIdInvalid):
        logger.info(f"{user_id} : User unreachable or invalid.")
        return 400
    except Exception as e:
        logger.error(f"Failed to send to {user_id} : {e}")
        return 500
