# 2. Прикрутить бота к задачам с предыдущего семинара:
# 1. Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
# 2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from write_data import *

updater = Updater("5469356678:AAHAkSjo3A_RjPr3EDJxYvsKDqwvUSo8l70")
updater.dispatcher.add_handler(CommandHandler("write", w_command))
# updater.dispatcher.add_handler(CommandHandler("read", r_command))
# updater.dispatcher.add_handler(CommandHandler("delete", d_command))
# updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
print("server run")
updater.start_polling()
updater.idle()