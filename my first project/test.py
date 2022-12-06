import types
from telebot import types
import telebot
import sef_test

bot = telebot.TeleBot('5859139943:AAGGbirEUJzc1YvmrXc99oyYaDFiA6b4W0E')

mess = '0 - Exit\n1 - Repeat this message\n2 - Add one apple to cart (apple price is 1$)\n3 - Remove one apple from cart\n4 - Add one chocolate to cart (chocolate price is 3$)\n5 - Remove one chocolate from cart\n6 - Show my cart\n7 - Show checkout information'




@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.chat.id, mass)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn0 = types.KeyboardButton('0 - Exit')
    itembtn1 = types.KeyboardButton('1 - Repeat this message')
    itembtn2 = types.KeyboardButton('2 - Add one apple to cart')
    itembtn3 = types.KeyboardButton('3 - Remove one apple from cart')
    itembtn4 = types.KeyboardButton('4 - Add one chocolate to cart')
    itembtn5 = types.KeyboardButton('5 - Remove one chocolate from cart')
    itembtn6 = types.KeyboardButton('6 - Show my cart')
    itembtn7 = types.KeyboardButton('7 - Show checkout information')
    markup.add(itembtn0, itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def sendmessage(message):
    if message.text == '0 - Exit':
        sef_test.dell_chapp(message.chat.id)
        sef_test.dell_chch(message.chat.id)
        bot.send_message(message.chat.id, "EXIT - Your chart is empathy")
    elif message.text == '1 - Repeat this message':
        bot.send_message(message.chat.id, mess)
    elif message.text == '2 - Add one apple to cart':
        bot.send_message(message.chat.id, f'You have {sef_test.addapp(message.chat.id)} apples')
    elif message.text == '3 - Remove one apple from cart':
        if sef_test.can_rev_apple(message.chat.id):
            bot.send_message(message.chat.id, f'You have {sef_test.revapp(message.chat.id)} apples')
        else:
            bot.send_message(message.chat.id, "You don't have apples")
    elif message.text == '4 - Add one chocolate to cart':
        bot.send_message(message.chat.id, f'You have {sef_test.addch(message.chat.id)} chocolates')
    elif message.text == '5 - Remove one chocolate from cart':
        if sef_test.can_rev_ch(message.chat.id):
            bot.send_message(message.chat.id, f'You have {sef_test.revch(message.chat.id)} chocolates')
        else:
            bot.send_message(message.chat.id, "You don't have chocolates")
    elif message.text == '6 - Show my cart':
        bot.send_message(message.chat.id, f'You have {sef_test.chekapp(message.chat.id)} apples\nYou have {sef_test.chekch(message.chat.id)} chocolates')
    elif message.text == '7 - Show checkout information':
        bot.send_message(message.chat.id, f'Applse:             {sef_test.priceapp(message.chat.id)}$\nChocolates:      {sef_test.pricech(message.chat.id)}$\n________________\nPay:                   {sef_test.priceapp(message.chat.id) + sef_test.pricech(message.chat.id)}$')
        @bot.message_handler(commands=['button']):




bot.polling(none_stop=True)
