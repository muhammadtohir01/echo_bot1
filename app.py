from flask import Flask,request
import requests
from telegram import Bot,Update
from  telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters
import os
from echo import start,Lavash,CheeseBurger,GamBurger,XotDog,Buyurtma,Location

from bot_main import(
    start,
    echo,
)

app=Flask(__name__)
TOKEN=os.environ['TOKEN']
bot=Bot(TOKEN)


@app.route('/ali',methods=['POST','GET'])
def webhook():
    if request.method == 'GET':
        return 'Helo World'
    elif request.method == 'POST':

        data = request.get_json(force=True)

        dispatcher:Dispatcher = Dispatcher(bot, None , workers=0)

        update:Update = Update.de_json(data, bot)

        dispatcher.add_handler(CommandHandler('start',callback=start))
        dispatcher.add_handler(MessageHandler(Filters.text,echo))

        dispatcher.process_update(update)

        # chat_id = update.message.chat_id
        # text = update.message.text
        # if text !=None:

        #     bot.send_message(chat_id, text)
        # print(chat_id)
        dispatcher.add_handler(CommandHandler('start',start))
        dispatcher.add_handler(MessageHandler(Filters.text('Lavash'),Lavash))
        dispatcher.dispatcher.add_handler(MessageHandler(Filters.text('Cheese Burger'), CheeseBurger))
        dispatcher.dispatcher.add_handler(MessageHandler(Filters.text('Gam Burger'), GamBurger))
        dispatcher.dispatcher.add_handler(MessageHandler(Filters.text('Xot Dog'), XotDog))
        dispatcher.dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma'),Buyurtma))
        dispatcher.dispatcher.add_handler(MessageHandler(Filters.text('Location'),Location))
        dispatcher.start_polling()
        dispatcher.idle()
    return "Assalomu alaykum"