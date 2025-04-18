FROM python:3.10-slim

# Install system dependencies (FFmpeg and basic tools)
RUN apt update && apt install -y --no-install-recommends \
    ffmpeg \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your bot's source code
COPY . .

# Start the bot
CMD ["python", "bot.py"]
