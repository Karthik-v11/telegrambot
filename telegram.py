ADAFRUIT_IO_USERNAME = "_Karthik_"
ADAFRUIT_IO_KEY = "aio_kBPF12zGl4lYZGGfRVskniHijb72"
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
amn=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
def on(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=1))
  bot.send_message(chat_id=chat_id,text = "LIGHT IS TURNED ON")
def off(bot,update):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=0))
  bot.send_message(chat_id=chat_id,text = "LIGHT IS TURNED OFF")
  
updater = Updater('1677218080:AAGfZIkt3EVaEmlwp357nLsyu3BGi-KOW8w')
dp=updater.dispatcher
dp.add_handler(CommandHandler('On',on))
dp.add_handler(CommandHandler('Off',off))
updater.start_polling()
updater.idle()
