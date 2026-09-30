import telebot
from telebot import types

# আপনার বটের টোকেন
TOKEN = "8376308044:AAHuFai8EErp1BiqoF7hsfnX2hcRHGWFs6Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # ইনলাইন কিবোর্ড মেনু তৈরি
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn_get_number = types.InlineKeyboardButton("📞 Get Number", callback_data="get_number")
    btn_search_number = types.InlineKeyboardButton("🔍 Search Number", callback_data="search_number")
    btn_traffic = types.InlineKeyboardButton("🌐 Traffic", callback_data="traffic")
    btn_2fa = types.InlineKeyboardButton("🛡️ 2FA Online", callback_data="2fa_online")
    btn_refer = types.InlineKeyboardButton("🎁 Refer", callback_data="refer")
    btn_profile = types.InlineKeyboardButton("👤 My Profile", callback_data="my_profile")
    btn_support = types.InlineKeyboardButton("📱 Support", callback_data="support")
    
    markup.add(btn_get_number, btn_search_number)
    markup.add(btn_traffic, btn_2fa)
    markup.add(btn_refer, btn_profile)
    markup.add(btn_support)
    
    welcome_text = "✨ **Nexora Shop**-এ আপনাকে স্বাগতম!\n\nদয়া করে নিচের অপশনগুলো থেকে আপনার পছন্দমতো সার্ভিস সিলেক্ট করুন:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# সাপোর্ট অপশন হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: call.data == "support")
def callback_support(call):
    support_text = "📞 যেকোনো সাহায্যের জন্য যোগাযোগ করুন: @rabbi_com1"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, support_text)

# বট রান করার জন্য
if __name__ == "__main__":
    print("Nexora Shop Bot is running successfully...")
    bot.infinity_polling()

