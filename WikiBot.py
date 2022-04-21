import wikipedia
import telebot

wikipedia.set_lang('ru')
bot = telebot.TeleBot('5350482327:AAEtUXYGC7AbBHOUMumBrm3bqIE6ra6z-3U')


@bot.message_handler(commands=['start'])
def start(message):
    sending_mess = f"<b> Привіт{message.from_user.first_name}!</b>\n Щоб почати роботу введіть слово,що ви бажаєте знайти"
    bot.send_message(message.chat.id, sending_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    word = message.text.strip().lower()
    try:
        final_message = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_message = ""
    bot.send_message(message.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
