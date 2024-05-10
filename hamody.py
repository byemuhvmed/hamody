import telebot, requests
from telebot import types

token = "7138608701:AAE-n4A1EseuDNmRimcIex6hcu4FBrG8dLk"
bot = telebot.TeleBot(token)
url_repo = "https://m.facebook.com/help/contact/209046679279097"

def send_message(chat_id, text):
    bot.send_message(chat_id, text)

@bot.message_handler(commands=[ start ])
def start(message):
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/25",caption="""
✅ | مرحباً بك عزيزي في بوت Facebook عن الفيسبوك
📲 | ارسل رابط URL الخاص بالمستخدم
""")
    bot.register_next_step_handler(message, url_fb)

def url_fb(message):
    user_input = {"url": message.text}
    if not user_input["url"].startswith("https"):
        send_message(message.chat.id, """
🚨 | رابط غير صالح !!! 
""")
        return bot.register_next_step_handler(message, url_fb)
    send_message(message.chat.id, "🔊 |ارسل الاسم الكامل الخاص بالشخص المراد عنة")
    bot.register_next_step_handler(message, names, user_input)

def names(message, user_input):
    user_input["name"] = message.text
    send_message(message.chat.id, "📩 | ارسل الايميل الخاص بك للتواصل معك :")
    bot.register_next_step_handler(message, emails, user_input)

def emails(message, user_input):
    user_input["email"] = message.text
    if not "@" in user_input["email"]:
        send_message(message.chat.id, "⛔ | الايميل غير صالح")
        return bot.register_next_step_handler(message, emails, user_input)
    send_message(message.chat.id, "💻 | زودنا بمعلومات اضافيه :")
    bot.register_next_step_handler(message, sentreq, user_input)

def sentreq(message, user_input):
    other = message.text
    data = {
        "crt_url": user_input["url"],
        "crt_name": user_input["name"],
        "cf_age": " Less than 9 Years ",
        "Field255260417881843": other,
        "Field166040066844792": user_input["email"],
        "submit" : "submit"
    }
    response = requests.post(url_repo, data=data)
    if response.status_code == 200:
        send_message(message.chat.id, """
✅ | تم ارسال بنجاح
⚜️ | سيتم التواصل معك عبر الايميل
👁️ | المطور : @MH_BP
""")
    else:
        send_message(message.chat.id, """
🚫 | حدث خطأ يرجى المحاولة لاحقاً
""")
if __name__ == "__main__":
    bot.polling(none_stop=True)
