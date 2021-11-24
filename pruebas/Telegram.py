import requests
import qrcode
from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
)

updater = Updater(token='2122160333:AAHwMtZi4r8019lUyyvD27P9hezA3U8_2Rg', use_context=True)
dispatcher = updater.dispatcher


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')


def get_account(update, context):
    url = 'http://172.23.0.42:8087/api/comex/saldo?nroCuenta=1000008783&tipoDeCuenta=1'
    data = ""
    resp = requests.get(url)
    mi_diccionario = resp.json()

    for clave, valor in mi_diccionario.items():
        linea = "{_clave}:\t {_valor} \n".format(_clave = clave, _valor = valor)
        data = data +  linea 
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=data)


def get_qr(update, context):
    data = " ".join(context.args)
    img = qrcode.make(data)
    img.save("qr.png")
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('qr.png', 'rb'))


def start(update, context):
    keyboard = [["/hola"], ["/dame_cuenta"], ["/dame_qr"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)
    update.message.reply_text("Hola!", reply_markup=reply_markup)


start_handler = CommandHandler('start', start)
hello_handler = CommandHandler('hola', hello)
get_account_handler = CommandHandler('dame_cuenta', get_account)
get_qr_handler = CommandHandler('dame_qr', get_qr)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(get_account_handler)
dispatcher.add_handler(get_qr_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()
