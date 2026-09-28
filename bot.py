import os
import random
import telebot

# Token Render-dan awtomatiki alynýar
TOKEN = os.environ.get("8213708118:AAHuLSXSAGDQUFO0fGzaFyF4ePOIbiCmg9Y")
bot = telebot.TeleBot(8213708118:AAHuLSXSAGDQUFO0fGzaFyF4ePOIbiCmg9Y)


@bot.message_handler(commands=["start"])
def send_code(message):
    user_name = message.from_user.first_name
    generated_code = random.randint(100000, 999999)

    text = (
        f"Salam, {user_name}!\n\n"
        f"Hoş geldiňiz! Siziň aýratyn kodyňyz: **{generated_code}**"
    )

    bot.reply_to(message, text, parse_mode="Markdown")


bot.polling(non_stop=True)
