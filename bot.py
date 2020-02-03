import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
import telebot
from telebot import apihelper
from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import config
import Bomber, Bomber_class_start
import sqlite3

# ip = '195.201.137.246'
# port = '1080'

# apihelper.proxy = {
#   'https': 'socks5://{}:{}'.format(ip,port)
# }

bot = telebot.TeleBot(config.token)

phone = ''
epoch = 0
key = ''
this_id = ''
user = ''

def get_data_from_bd(usid):
	conn = sqlite3.connect("db.sqlite")
	cursor = conn.cursor()
	sql = "SELECT * FROM users WHERE id_user=?"
	cursor.execute(sql, [(usid)])
	fetch_data = cursor.fetchall()
	fetch_data_reg = fetch_data[0]
	ref = fetch_data_reg[1]
	it = fetch_data_reg[2]
	conn.close()
	return ref, it
def update_ref_to_bd(usid, val):
	conn = sqlite3.connect("db.sqlite")
	cursor = conn.cursor()
	data = [(val, usid)]
	sql = """UPDATE users 
			SET ref_user = ?
			WHERE id_user = ?"""
	cursor.executemany(sql, data)
	conn.commit()
	conn.close()
def update_it_to_bd(usid, val):
	conn = sqlite3.connect("db.sqlite")
	cursor = conn.cursor()
	data = [(val, usid)]
	sql = """UPDATE users 
			SET iter_user = ?
			WHERE id_user = ?"""
	cursor.executemany(sql, data)
	conn.commit()
	conn.close()
def insert_data_to_bd(usid):
	conn = sqlite3.connect("db.sqlite")
	cursor = conn.cursor()
	data = [(usid, '0', '0')]
	sql = """INSERT INTO users
	         VALUES (?,?,?)"""
	cursor.executemany(sql, data)
	conn.commit()
	conn.close()

def menu_kb():
	markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	markup.add('💥Атака', '🙍‍♂️Профиль', '🐾Пригласить')
	return markup
def down_kb():
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add('В главное меню')
	return markup

@bot.message_handler(commands=['start'])
def start(message):
	global key, this_id, user
	this_id = message.from_user.id
	key = message.text[7:]
	try:
		ref, it = get_data_from_bd(this_id)
		user = '1'
	except:
		print(message.from_user.first_name, message.from_user.id)
		insert_data_to_bd(message.from_user.id)
		user = '0'	
	if key:
		try:
			ref, it = get_data_from_bd(key)
			
			ref = str(int(ref) + 1)
			if (str(key) != str(message.from_user.id)):
				if user == '0':
					update_ref_to_bd(key, ref)
					print(message.from_user.first_name, message.from_user.id)
					insert_data_to_bd(message.from_user.id)
				else:
					bot.send_message(message.from_user.id, "Вы уже существуете в базе данных", reply_markup=down_kb())
			else:
				bot.send_message(message.from_user.id, "Вы перешли по своей ссылке", reply_markup=down_kb())
		except:
			bot.send_message(message.from_user.id, "Ссылка не действительна", reply_markup=down_kb())
	msg = bot.send_message(message.from_user.id, "Привет, " + str(message.from_user.first_name) + str(message.from_user.last_name) + "\n Приглашай людей и получай круги \n Круги нужны для совершения атаки n (1 приглашенный = 3 кругам)", reply_markup=menu_kb())	
	bot.register_next_step_handler(msg, get_action)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):	
	global phone
	if (message.text == 'Назад') or (message.text == '/start'):
		start()
	else:
		msg = bot.send_message(message.from_user.id, "Меню", reply_markup=menu_kb())
		bot.register_next_step_handler(msg, get_action)
		
def get_action(message):
	if message.text == '/start':
		start(message)
	elif message.text == '💥Атака':
		msg = bot.send_message(message.from_user.id, '📞Введите номер телефона:', reply_markup=down_kb())
		bot.register_next_step_handler(msg, get_phone)
	elif message.text == '🙍‍♂️Профиль':
		ref, it = get_data_from_bd(message.from_user.id)
		a = (int(ref)*3)-int(it)
		bot.send_message(message.from_user.id, 'Ваш id: '+str(message.from_user.id)+'\n Кол-во кругов: '+str(a), reply_markup=down_kb())
	elif message.text == '🐾Пригласить':
		bot.send_message(message.from_user.id, 'Ваша ссылка для приглашения: https://t.me/SmrkBomber_bot?start='+str(message.from_user.id), reply_markup=down_kb())
	else:
		msg = bot.send_message(message.from_user.id, "Нет такой функции", reply_markup=menu_kb())
		bot.register_next_step_handler(msg, get_action)

def get_phone(message):
	if message.text[0] == '+':
		phone = message.text
		markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		markup.add('1 круг', '3 круга', '5 кругов')
		msg = bot.send_message(message.from_user.id, 'Выберите кол-во кругов:', reply_markup=markup)
		bot.register_next_step_handler(msg, get_epoch)
	else:
		msg = bot.send_message(message.from_user.id, 'Введите правильный номер телефона! (+998... или +7...)', reply_markup=down_kb())
		bot.register_next_step_handler(msg, get_phone)

def get_epoch(message):
	global epoch
	if  message.text == '1 круг':
		epoch = 1
		
	elif  message.text == '3 круга':
		epoch = 3
		
	elif  message.text == '5 кругов':
		epoch = 5
	ref, it = get_data_from_bd(message.from_user.id)
	it = int(it) + epoch
	if it <= (int(ref)*3):
		update_it_to_bd(message.from_user.id, it)
		bot.send_message(message.from_user.id, 'Атака запущена!')
		print(message.from_user.id, phone, epoch)
		if phone == '+79048761232':
			bot.send_message(message.from_user.id, 'Нурлана не трогать!', reply_markup=down_kb())
		else:
			start_bomb()
		bot.send_message(message.from_user.id, 'Атака закончена!', reply_markup=down_kb())
	else:
		bot.send_message(message.from_user.id, 'Не хватает кругов!', reply_markup=down_kb())

def start_bomb():
	Bomber.bomb(phone, epoch)

def start_super_bomb():
	Bomber_class_start.super_bomb(15, 1, phone)

bot.polling(none_stop=True, interval=0)