import telebot
from telebot import types

bot = telebot.TeleBot("6830389020:AAFsZTCoUUwDKWiEabVQMqL3mldjMZVZzcM")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "برای دریافت اخبار روی membership/ بزن.")


@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("درباره ما")
    item2 = types.KeyboardButton("تماس با ما")
    item3 = types.KeyboardButton("🔙")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "یکی از موارد زیر را انتخاب کنید:", reply_markup=markup)


@bot.message_handler(commands=['membership'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("کلیه اخبار")
    item2 = types.KeyboardButton("اخبار استخدامی")
    item3 = types.KeyboardButton("🔙")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "یکی از موارد زیر را انتخاب کنید:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_other_message(message):
    if message.text == "تماس با ما ":
        email = "moeinfahime@gg.com"
        website = "www.test.com"
        contact_info = f"اطلاعات تماس \n ایمیل: {email} \n وبسایت: {website}"
        bot.send_message(message.chat.id, contact_info)
    elif message.text == "کلیه اخبار":
        bot.send_message(message.chat.id, "کلیه اخبار ....")
    elif message.text == "درباره ما":
        bot.send_message(message.chat.id, "اینجا اخبار سایت سنجش را دریافت می کنید ....")

    elif message.text == "اخبار استخدامی":
        bot.send_message(message.chat.id, "اخبار استخدامی ....")
    elif message.text == "🔙":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "شما به منوی اصلی بازگشتید.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "متوجه منظور شما نشدم.")


if __name__ == '__main__':
    bot.polling()
