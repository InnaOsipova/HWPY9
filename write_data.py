import csv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext



def write (update: Update, context: CallbackContext):
    record =[]
    table = ['last_name', 'name', 'phone_number', 'post', "salary"]
    for i in range(len(table)):
        update.message.reply_text(table[i])
        msg = update.message.text
        record.append(msg)
    return record

def w_command(update: Update, context: CallbackContext):
    
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(write())
    update.message.reply_text('Данные успешно записаны')
    print("Данные успешно записаны")
    return 