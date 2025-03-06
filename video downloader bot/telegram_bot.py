import requests
import os
import yt_dlp
from pyrogram import Client, filters
# Bot tokeni
BOT_TOKEN = "7824640514:AAFnOlkQ7s8V4bSMVa_ULiiTT5sRYrXcTM8"
API_ID = 21639704  # my.telegram.org saytidan olingan API_ID
API_HASH = "68e32436ff2dc04215bae10843793195"  # my.telegram.org saytidan olingan API_HASH
# Botni ishga tushirish
app = Client("video_downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
# Video yuklab olish va yuborish funksiyasi
@app.on_message(filters.text)
async def download_video(client, message):
    url = message.text.strip()  # Foydalanuvchi yuborgan link
    if any(site in url for site in ["youtube.com", "youtu.be", "instagram.com", "tiktok.com"]):
        await message.reply_text("⏳ Video yuklab olinmoqda...")
        # Video yuklab olish sozlamalari
        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
        video_path = None
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info).replace(".webm", ".mp4").replace(".mkv", ".mp4")
        # Yuklangan fayl borligini tekshirish
        if video_path and os.path.exists(video_path):
            await message.reply_video(video_path, caption="✅ Video tayyor!")
            os.remove(video_path)  # Faylni o'chirish
        else:
            await message.reply_text("❌ Video yuklab olinmadi!")
    else:
        await message.reply_text("❌ Iltimos, faqat Instagram, TikTok yoki YouTube videoning linkini yuboring.")
# Botni ishga tushirish
app.run()