import telebot
import time

# বটের টোকেন
TOKEN = '8376308044:AAHuFai8EErp1BiqoF7hsfnX2hcRHGWFs6Q'

# সাপোর্ট এডমিন ইউজারনেম
ADMIN_USERNAME = "@rabbi_com1"

bot = telebot.TeleBot(TOKEN)

# স্টার্ট কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "👋 হ্যালো! আমাদের বটে আপনাকে স্বাগতম।\n\n"
        "যেকোনো তথ্যের জন্য নিচের কমান্ডগুলো ব্যবহার করুন:\n"
        "🔹 /support - সাপোর্ট এডমিনের সাথে যোগাযোগ\n"
        "🔹 /help - বটের সাহায্য পেতে"
    )
    bot.reply_to(message, welcome_text)

# সাপোর্ট ও হেল্প কমান্ড
@bot.message_handler(commands=['support', 'help', 'admin'])
def send_support(message):
    support_text = (
        "🛠 সাপোর্ট সেন্টার\n\n"
        "আপনার যেকোনো সমস্যা বা প্রশ্নের জন্য সরাসরি আমাদের সাপোর্ট এডমিনের সাথে যোগাযোগ করুন:\n"
        f"👤 এডমিন: {ADMIN_USERNAME}"
    )
    bot.reply_to(message, support_text)

# সাধারণ মেসেজ ইকো
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# ফাস্ট রিপ্লাই ও অটো-রিস্টার্ট সহ বট চালু রাখা
while True:
    try:
        print("বট সর্বোচ্চ স্পিডে চালু আছে...")
        bot.polling(none_stop=True, interval=0, timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"ভুল বা নেটওয়ার্ক সমস্যা হয়েছে: {e}")
        time.sleep(2)
