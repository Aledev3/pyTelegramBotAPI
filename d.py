import telebot

@bot.message_handler(commands=["f"])
def _f(message):
  bot.send_message(message.chat.id, message.photo)


print("hello world")

