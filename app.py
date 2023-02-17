from flask import Flask,request
import requests
from telegram import Bot,Update
from  telegram.ext import Dispatcher,CommandHandler,MessageHandler,Filters
import os
from echo import start,Lavash,CheeseBurger,GamBurger,XotDog,Buyurtma,Location,Nomer


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


        dispatcher.add_handler(CommandHandler('start',start))
        dispatcher.add_handler(MessageHandler(Filters.text('Lavash'),Lavash))
        dispatcher.add_handler(MessageHandler(Filters.text('Cheese Burger'), CheeseBurger))
        dispatcher.add_handler(MessageHandler(Filters.text('Gam Burger'), GamBurger))
        dispatcher.add_handler(MessageHandler(Filters.text('Xot Dog'), XotDog))
        dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma'),Buyurtma))
        dispatcher.add_handler(MessageHandler(Filters.text('Location'),Location))
        dispatcher.add_handler(MessageHandler(Filters.text('Nomer'),Nomer))
        dispatcher.process_update(update)
    return "Assalomu alaykum"