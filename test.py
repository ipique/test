import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
        bot.send_message(message.from_user.id, "Psss.. ")

@bot.message_handler(commands=["getsignal"])
def getsignal(message):
        key = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton(text="Payment",url="https://google.com")
        key.add(button_1)
        bot.send_message(message.from_user.id, "You can just copy address 0xf4723db6a2655ff89ca4a39c4683d94c1b046630 and pay via your wallet, or use API", reply_markup=key)
