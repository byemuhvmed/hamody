"""
Rate :- @DF_GD_D 
Channel :- @T62RS 
In :- 2024/4/1
"""
import telebot, os, re, yt_dlp
from dotenv import load_dotenv
from telebot import types
load_dotenv()
token = "7138608701:AAE-n4A1EseuDNmRimcIex6hcu4FBrG8dLk" 
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    welcome_message = """
👋 | مرحبا بك عزيزي 
🗣️ | يمكنك من خلال البوت تحميل المقاطع الفيديو من منصه X
🌙 | ارسل رابط المقطع للتحميل 
☝️ | المعدل : @MH_BP
"""
    bot.send_photo(message.chat.id, "https://t.me/ifuwufuj/31", caption=welcome_message)
@bot.message_handler(func=lambda message: re.match(r'.*(?:https?\:\/\/)?(?:www\.)?(?:x\.com)\/(\w+)\/status(?:es)?\/(\d+)(?:\?s=\d+)?', message.text))
def download_x_video(message):
    try:
        msg = bot.send_message(message.chat.id, "🌟 | جار تهيئة المقطع والتحميل...")
        match = re.match(r'.*(?:https?\:\/\/)?(?:www\.)?(?:x\.com)\/(\w+)\/status(?:es)?\/(\d+)(?:\?s=\d+)?', message.text)
        content_id = match.group(2)
        content_type = match.group(1)
        content_url = f"https://x.com/{content_type}/status/{content_id}"
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(content_url, download=False)
            name = info.get('title', 'video_descargado')
            filepath = ydl.prepare_filename(info)
        bot.send_video(message.chat.id, filepath, caption=name)
        os.remove(filepath)
    except Exception as e:
        error_message = f"""
⛔ | حدث خطأ أثناء التحميل 
🤖 | رمز الخطأ : {e}
"""
        bot.send_message(message.chat.id, error_message)
    finally:
        bot.delete_message(message.chat.id, msg.message_id)
if __name__ == '__main__':
    print("Running")
    bot.polling(none_stop=True)
"""
Rate :- @DF_GD_D 
Channel :- @T62RS 
In :- 2024/4/1
"""