import sqlite3
import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup
import time

bot=telebot.TeleBot("5306404487:AAHNVixDQRusl_jNpcAwt2Ws010YruG2Qxs")

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id:int, User_firstname: str, User_surname: str, Username: str,Password:str,Role:str,User_Class:str):
	cursor.execute('INSERT OR IGNORE INTO Users (user_id,User_firstname, User_surname, Username,Password,Role,User_Class) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, User_firstname, User_surname, Username, Password, Role, User_Class))
	conn.commit()







@bot.message_handler(commands=['start'])
def start_message(message):
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEol5ic--KCl5S4M7VikHIi0c0ojAwLQACwBYAArDSuEjJW95g75GuOiQE")
        bot.send_message(message.chat.id,"Привет,я Джей")
        keyboard=ReplyKeyboardMarkup(True)
        keyboard.row('/Погнали')
        
        bot.send_message(message.chat.id,"Для начала давай познакомимся",reply_markup=keyboard)


    


@bot.message_handler(commands=['Погнали'])
def get_text_messages(message):
        bot.send_message(message.chat.id,"Напиши класс ,в котором ты учишься") 
        bot.register_next_step_handler(message,registration)


def registration(message):
        registration=message.text.split()
        bot.send_message(message.from_user.id,"Обработка...")
        us_id=message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        password = "-"
        role = "Ученик"
        user_Class = registration[0]

        db_table_val(user_id=us_id,User_firstname=us_name, User_surname=us_sname, Username=username, Password=password, Role=role, User_Class=user_Class)

        bot.send_message(message.chat.id,"Продолжим!")
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEtlVifSdwwHUvZhADOyu8xBaeRjTogQACeBQAAn1ziUixSPOhsVgHpSQE")
        markup1=telebot.types.InlineKeyboardMarkup()
        markup1=ReplyKeyboardMarkup(True)
        markup1.row('/Староста','/Ученик')
        bot.send_message(message.chat.id,"Какая у тебя должность?",reply_markup=markup1)

@bot.message_handler(commands=["Староста"])
def starosta(message):
        bot.send_message(message.chat.id,"Не узнаю тебя,сначала скажи пароль!")
        bot.register_next_step_handler(message,starosta_password)


def starosta_password(message):
        
        
        
                

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEvARigVjQhXUQ7EoxgEm6G2hQPdR-7QAC4xkAAryZsElf5GOjAAIyMSQE")
    bot.send_message(message.chat.id,"Вот функции которые я могу выполнить\n /check_your_raspisanie блаблаблаблабла")

@bot.message_handler(commands=['end'])
def end_message(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEEvApigVtFCRdnMzvJ1CPT2IerZRu-PwACthIAAuRUyUtPd5qr1_V8cSQE")
    bot.send_message(message.chat.id,"Уже уходишь?.Может не нада?(((")


def auth(message):
    
    password=registration[0]
    role="Староста"
    user_C=registration[1]

    db_role_(Password=password,Role=role,User_Class=user_C)

def auth1(message):
        password="0"
        role="Ученик"
        user_C= message.text
    
        db_role_(Password=password,Role=role,User_Class=user_C)

@bot.callback_query_handler(func=lambda call:True)
def whoareyoy(call):
    if call.data=="starosta":
        bot.send_message(call.message.chat.id,"/starosta")
        

    '''if call.data=="uchenik":
        bot.send_message(message.chat.id,"Из какого ты класса?")
        bot.register_next_step_handler(message,auth1)'''
       
@bot.message_handler(commands=['starosta'])
def starosta(message):
        bot.send_message(message.chat.id,"Напиши придуманный пароль и класс,в котором ты учишься через запятую следующим сообщением\nПример: чебурек22367,9в")
        bot.register_next_step_handler(message,auth)





'''keyboard=ReplyKeyboardMarkup(True)
keyboard.row('/help','/test','/end')
bot.send_message(message.chat.id,"Мяу)",reply_markup=keyboard)'''

   

    
'''Напиши придуманный пароль и класс,в котором ты учишься через запятую следующим сообщением\nПример: чебурек22367,9в'''










bot.polling(non_stop=True)
