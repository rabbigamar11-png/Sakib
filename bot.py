import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# আপনার টেলিগ্রাম বট টোকেনটি এখানে বসান
BOT_TOKEN = "8376308044:AAHuFai8EErp1BiqoF7hsfnX2hcRHGWFs6Q"
bot = telebot.TeleBot(BOT_TOKEN)

# ইমেইল স্টক (এখানে বিক্রির ইমেইলগুলো জমা থাকবে)
mail_stock = [
    "example1@gmail.com : pass123",
    "example2@gmail.com : pass456"
]

# ইউজারের ব্যালেন্স ট্র্যাক করার জন্য (মেমোরি ডাটাবেজ)
user_balances = {}

# /start কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 0.0  # নতুন ইউজারদের ব্যালেন্স 0

    # প্রধান মেনু বাটন (Reply Keyboard)
    main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.row("🛍️ Buy Products")
    main_menu.row("👤 My Profile", "💳 Deposit")
    main_menu.row("🔑 Get Code", "💬 Support")

    bot.send_message(
        message.chat.id,
        f"👋 **স্বাগতম {message.from_user.first_name}!**\n\nআমাদের অটো-সেলিং বটে আপনাকে স্বাগতম। নিচের মেনু থেকে অপশন সিলেক্ট করুন।",
        parse_mode="Markdown",
        reply_markup=main_menu
    )

# টেক্সট কমান্ড হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    user_id = message.from_user.id
    
    if message.text == "🛍️ Buy Products":
        # প্রোডাক্ট ক্যাটাগরি (Inline Keyboard)
        markup = InlineKeyboardMarkup()
        btn_vpn = InlineKeyboardButton("🛡️ VPN", callback_data="buy_vpn")
        btn_proxy = InlineKeyboardButton("🌐 Proxy", callback_data="buy_proxy")
        btn_mail = InlineKeyboardButton("✉️ Mail", callback_data="buy_mail")
        btn_other_mail = InlineKeyboardButton("📧 Other Domain Mail", callback_data="buy_other_mail")
        btn_rec_mail = InlineKeyboardButton("📬 Recovery Added Mail", callback_data="buy_rec_mail")

        markup.row(btn_vpn, btn_proxy)
        markup.row(btn_mail)
        markup.row(btn_other_mail, btn_rec_mail)

        bot.send_message(message.chat.id, "🛍️ **Buy Products**\n\nSelect a category:", parse_mode="Markdown", reply_markup=markup)

    elif message.text == "👤 My Profile":
        balance = user_balances.get(user_id, 0.0)
        bot.send_message(
            message.chat.id,
            f"👤 **আপনার প্রোফাইল Information:**\n\n🆔 **User ID:** `{user_id}`\n💰 **Balance:** {balance} BDT",
            parse_mode="Markdown"
        )

    elif message.text == "💳 Deposit":
        bot.send_message(
            message.chat.id,
            "💳 **টাকা জমা/Deposit করার নিয়ম:**\n\nবিকাশ/নগদ নাম্বার: `017XXXXXXXX` (Send Money)\nটাকা পাঠানোর পর এডমিনকে ট্রানজেকশন আইডি পাঠান।",
            parse_mode="Markdown"
        )

    elif message.text == "💬 Support":
        bot.send_message(message.chat.id, "💬 যেকোনো সাহায্যের জন্য যোগাযোগ করুন: @rabbi_com1")

# ইনলাইন বাটন ক্লিক হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    user_id = call.from_user.id

    if call.data == "buy_mail":
        # ইমেইলের দাম ধরে নিলাম ১০ টাকা
        price = 10.0
        current_balance = user_balances.get(user_id, 0.0)

        if current_balance < price:
            bot.answer_callback_query(call.id, "❌ আপনার পর্যাপ্ত ব্যালেন্স নেই! আগে Deposit করুন।", show_alert=True)
        else:
            if mail_stock:
                mail = mail_stock.pop(0)  # স্টক থেকে একটি ইমেইল বের করবে
                user_balances[user_id] -= price
                bot.send_message(
                    call.message.chat.id,
                    f"✅ **ইমেইল ক্রয় সফল হয়েছে!**\n\n📦 **আপনার প্রোডাক্ট:**\n`{mail}`\n\n💰 অবশিষ্টাংশ ব্যালেন্স: {user_balances[user_id]} BDT",
                    parse_mode="Markdown"
                )
            else:
                bot.answer_callback_query(call.id, "⚠️️ দুঃখিত, বর্তমানে ইমেইল স্টক খালি আছে!", show_alert=True)

bot.polling(none_stop=True)
