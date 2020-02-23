"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_constellation(bot, update):
    input = update.message.text.split()
    if len(input) > 1:
        planet = input[1].capitalize()
        today = update.message.date
        try:
            result = ephem.constellation(getattr(ephem, planet)(today))
            text = 'Cегодня {} в созвездии {}!'.format(planet, result[1])
            update.message.reply_text(text)
        except AttributeError:
            text = 'Такой планеты не существует'
            update.message.reply_text(text)
    else:
        text = 'Некорректный ввод'
        update.message.reply_text(text)

    logging.info('User: %s, Input: %s --> Output: %s',
                 update.message.chat.username, update.message.text, text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_constellation))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
