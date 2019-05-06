import telebot

token = '843098044:AAETHCfTVOP7I54vlDj8ydu9Yy1o3Jl1Aj0' # Вставь свой токен
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)