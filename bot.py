from pyrogram import Client, filters
import os

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("music") & filters.private)
def music_downloader(client, message):
    if len(message.command) < 2:
        message.reply("Send song name like this:\n/music faded")
        return

    query = message.text.split(" ", 1)[1]
    message.reply(f"🎵 Downloading: `{query}`...")

    os.system(f"yt-dlp -x --audio-format mp3 -o 'song.%(ext)s' 'ytsearch1:{query}'")

    if os.path.exists("song.mp3"):
        message.reply_audio("song.mp3", title=query)
        os.remove("song.mp3")
    else:
        message.reply("❌ Failed to download.")

app.run()
