from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize the bot client
app = Client(
    name="movie_filter_bot",  # Session name must be a string
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Import handlers directly (flat structure)
import start
import filter

# Optional: Keep a dummy port open to satisfy Render's web service requirement
import threading
import time
import socket

def keep_alive():
    s = socket.socket()
    s.bind(('0.0.0.0', 10000))  # Dummy port
    s.listen(1)
    while True:
        time.sleep(1000)

threading.Thread(target=keep_alive).start()

# Start the bot
if __name__ == "__main__":
    app.start()
    print("✅ Bot started successfully!")
    idle()
    app.stop()
    print("🛑 Bot stopped.")
