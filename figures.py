import telebot
from telebot import types
import os

bot = telebot.TeleBot('5754791918:AAG7LTncqI3Bz5LonwjMxRzSNC1y8xC7IXs')


@bot.message_handler(commands=["start"])
def oneq(message):
    bot.send_message(message.chat.id,
                     "Hello and welcome to the Official Spin Art bot who generates spin art. (Beta version, still working on it)")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Circle")
    btn2 = types.KeyboardButton("Square")
    btn3 = types.KeyboardButton("Triangle")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "What shape do you want?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Circle', 'Square', 'Triangle'])
def head_menu_buttons1(message):
    global shape
    shape = message.text
    if message.text == 'Circle' or message.text == 'Triangle' or message.text == 'Square':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Red')
        btn2 = types.KeyboardButton('Green')
        btn3 = types.KeyboardButton('Blue')
        main_menu = types.KeyboardButton('Main Menu')
        markup.add(btn1, btn2, btn3, main_menu)
        bot.send_message(message.chat.id, "What first color do you want?", reply_markup=markup)

    if message.text == 'Main Menu':
        oneq(message)


@bot.message_handler(func=lambda message: message.text in ['Red', 'Green', 'Blue', 'Main Menu (Restart)'])
def head_menu_buttons2(message):
    global firstcolor
    firstcolor = message.text
    if message.text == 'Red' or message.text == 'Green' or message.text == 'Blue':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Orange')
        btn2 = types.KeyboardButton('Yellow')
        btn3 = types.KeyboardButton('Purple')
        main_menu = types.KeyboardButton('Main Menu (Restart)')
        markup.add(btn1, btn2, btn3, main_menu)

        bot.send_message(message.chat.id, "What second color do you want?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Orange', 'Yellow', 'Purple', 'Main Menu (Restart)'])
def head_menu_buttons3(message):
    global secondcolor
    secondcolor = message.text
    if secondcolor == 'Orange' or message.text == 'Yellow' or message.text == 'Purple':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Pink')
        btn2 = types.KeyboardButton('Light Blue')
        btn3 = types.KeyboardButton('Lime')
        main_menu = types.KeyboardButton('Main Menu (Restart)')
        markup.add(btn1, btn2, btn3, main_menu)

        bot.send_message(message.chat.id, "What third color do you want?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Pink', 'Light Blue', 'Lime', 'Main Menu (Restart)'])
def head_menu_buttons4(message):
    global thirdcolor
    thirdcolor = message.text
    if thirdcolor == 'Pink' or message.text == 'Light Blue' or message.text == 'Lime':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        finish = types.KeyboardButton('Yes')
        main_menu = types.KeyboardButton('No (Restart)')
        markup.add(finish, main_menu)

        bot.send_message(message.chat.id, "Are you okay with combination?", reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text in ['Circle', 'Square', 'Triangle','Red', 'Green', 'Blue', 'Orange', 'Yellow', 'Purple','Pink', 'Light Blue', 'Lime', 'Yes', 'No (Restart)' 'Main Menu (Restart)' ])
    def head_menu_buttons4(message):

        if shape == 'Circle' and firstcolor == 'Red' and secondcolor == 'Orange' and thirdcolor == 'Pink' and message.text == 'Yes':
            bot.send_photo(message.chat.id,open("CST\Spin Art Bot Circles\circlered1.png", 'rb'))
        if shape == 'Circle' and firstcolor == 'Red' and secondcolor == 'Orange' and thirdcolor == 'Pink' and message.text == 'Yes':
            bot.send_photo(message.chat.id,open("CST/Spin Art Bot Triangle/triangleblue1.png", 'rb'))


if __name__ == '__main__':
    bot.infinity_polling()





