import re
import os
import time
from os import environ, getenv

# Regex to validate numeric IDs
id_pattern = re.compile(r'^.\d+$')

# Configuration class that holds all the necessary configurations
class Config(object):
    # Pyro Client Configuration
    API_ID = os.environ.get("API_ID", "20793620")
    API_HASH = os.environ.get("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Database Configuration
    DB_NAME = os.environ.get("DB_NAME", "Hunter")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    PORT = os.environ.get("PORT", "8080")

    # Other Configurations
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/29a3acbbab9de5f45a5fe.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6853851676 6186511950 6826093533').split()]
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', 'weoo_animes').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002523934652"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002411336159"))

    # Webhook Configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

# Text configurations for bot responses
class Txt(object):
    # Starting message text when user interacts with the bot
    START_TXT = """<b>ʜᴇʏ! {}

» ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ! ᴡʜɪᴄʜ ᴄᴀɴ ᴀᴜᴛᴏʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴀʟsᴏ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇᴍ ᴘᴇʀғᴇᴄᴛʟʏ</b>"""

    # File name setup guide message
    FILE_NAME_TXT = """<b>» <u>sᴇᴛᴜᴘ ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ ғᴏʀᴍᴀᴛ</u></b>

<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b> ➲ ᴇᴘɪꜱᴏᴅᴇ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ᴇᴘɪꜱᴏᴅᴇ ɴᴜᴍʙᴇʀ ➲ ꜱᴇᴀꜱᴏɴ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ꜱᴇᴀꜱᴏɴ ɴᴜᴍʙᴇʀ ➲ ǫᴜᴀʟɪᴛʏ - ᴛᴏ ʀᴇᴘʟᴀᴄᴇ ǫᴜᴀʟɪᴛʏ

<b>‣ ꜰᴏʀ ᴇx:- </b> /autorename Oᴠᴇʀғʟᴏᴡ [Sseason Eepisode] - [Dual] quality

<b>‣ /Autorename: ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ ʙʏ ɪɴᴄʟᴜᴅɪɴɢ 'ᴇᴘɪꜱᴏᴅᴇ' ᴀɴᴅ 'ǫᴜᴀʟɪᴛʏ' ᴠᴀʀɪᴀʙʟᴇꜱ ɪɴ ʏᴏᴜʀ ᴛᴇxᴛ, ᴛᴏ ᴇxᴛʀᴀᴄᴛ ᴇᴘɪꜱᴏᴅᴇ ᴀɴᴅ ǫᴜᴀʟɪᴛʏ ᴘʀᴇꜱᴇɴᴛ ɪɴ ᴛʜᴇ ᴏʀɪɢɪɴᴀʟ ꜰɪʟᴇɴᴀᴍᴇ. """

    # About text to provide bot details
    ABOUT_TXT = f"""<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/weoo_anime">ᴀᴜᴛᴏ ʀᴇɴᴀᴍᴇ</a>

❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/otakukart7">Hunter</a> ❍ ɢɪᴛʜᴜʙ : <a href="https://github.com">Hunter</a> ❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a> ❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a> ❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/weoo_anime">ᴠᴘs</a> ❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/weoo_animes">Weoo ᴀɴɪᴍᴇS</a>

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

    # Thumbnail setup guide
    THUMBNAIL_TXT = """<b><u>» ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>

➲ /start: ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ.. ➲ /del_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴᴀɪʟ. ➲ /view_thumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ

# Thumbnail setup guide (continued)
    THUMBNAIL_TXT += """ ᴛʜᴜᴍʙɴᴀɪʟ ᴡᴏʀᴋ ᴏᴠᴇʀᴋᴏᴏᴋ ᴠᴀʀɪᴀʙʟᴇꜱ ᴏɴᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

    ➻ ᴜsᴇ ᴛʜᴇ /autorename ᴠᴀʀɪᴀʙʟᴇ ᴏɴᴇ ᴄᴜsᴛᴏᴍ ᴄᴏᴍᴍᴀɴᴅᴇᴅ"""

    # Error messages for the bot
    ERROR_TXT = """<b>⚠️ Something went wrong! Try again or contact the administrator.</b>"""
    
    # Custom File Caption (where users can customize their captioning)
    CAPTION_TXT = """<b>ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ɢᴜɪᴅᴇ</b>
    
    ᴜsᴇ ʀᴇɴᴀᴍᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜᴇ ᴇᴘɪꜱᴏᴅᴇ! """

    # Commands for setting up file captions
    SET_CAPTION_TXT = """<b>use `format` to replace filename text"""

    # Auto-renaming options with description
    AUTO_RENAME_TXT = """<b>» Use /auto_rename to begin automatically renaming files for your preferred anime series.</b>"""

    # "Admin" commands that should be accessible only to Admin users
    ADMIN_CMDS = {
        "set_thumbnail": "/set_thumbnail - Set custom thumbnail for the bot.",
        "view_logs": "/view_logs - View logs.",
        "set_quality": "/set_quality - Set video quality (480p, 720p, 1080p)."
    }

# If you need to add more commands or information, you can easily extend this pattern.

# Bot's status messages that help admins keep track of the bot's operational status
class StatusMessages:
    BOT_STARTED = "Bot has started successfully."
    BOT_STOPPED = "Bot has been stopped."
    BOT_RESTARTED = "Bot has been restarted."

# File management-related text (useful for file renaming scenarios)
class FileManagement:
    FILE_RENAMED_SUCCESSFULLY = "File has been renamed successfully!"
    FILE_RENAMING_FAILED = "Failed to rename the file. Try again."
    FILE_QUALITY_SET = "File quality has been set."
    FILE_THUMBNAIL_SET = "Thumbnail has been set successfully."
    FILE_DELETED = "The file has been deleted."

# The following are helper functions for any additional functionality that might be needed

def get_admins():
    """
    This function returns the list of admin IDs configured in the environment.
    It's used to check permissions and perform actions that require admin privileges.
    """
    return Config.ADMIN

def get_subscribed_channels():
    """
    This function returns a list of channels that users must subscribe to in order to use the bot.
    """
    return Config.FORCE_SUB_CHANNELS

def is_webhook_enabled():
    """
    Returns whether webhook functionality is enabled based on environment variables.
    """
    return Config.WEBHOOK

# Add other utility functions as required
