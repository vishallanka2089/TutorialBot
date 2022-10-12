from email.message import Message
import os
from turtle import update
import requests
import telegram.ext
import telebot
from process import *
API_KEY = "5674217157:AAGkDfvbYAcu6xAPRxss1pZrbDsoRGROVL0"
bot = telebot.TeleBot(API_KEY)
session = {}

@bot.message_handler(commands=['start'])
def greet(message):
      bot.reply_to(message, 'Hey there! How are you!')

@bot.message_handler(commands=['help'])
def help(message):
      bot.reply_to(message, "Hi There! This is a simple bot that gives the details of Institute of aeronautical engineering.")
      bot.send_message(message.chat.id, "Type /brochure to get the college brochure\nType /placementnews to get latest placementnews news,\nType /academiccalender to get latest placementnews news\nType /programs to get list of programs avalailabe at iare\nType /location to get location of the college\nType /email to get principal's email.")

@bot.message_handler(commands=['placementnews'])
def placement(message):
      bot.reply_to(message, 'This is the latest placement news')
      bot.send_document(message.chat.id,"https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/notification/2022-23/Deltax.pdf")
@bot.message_handler(commands=['academiccalender'])
def academic(message):
      bot.reply_to(message, 'This is the latest placement news')
      bot.send_document(message.chat.id,"https://www.iare.ac.in/sites/default/files/AcademicCalendar2021/B.TECH_I_AND_II_SEMESTERS_ACADEMIC_CALENDAR_2021-2022_REVISED.pdf")
@bot.message_handler(commands=['programs'])
def programs(message):
      bot.reply_to(message, 'We offers B.tech and M.tech courses in CSE,IT,MECH.,ECE,EEE and MBA programs')
@bot.message_handler(commands=['location'])
def location(message):
      bot.reply_to(message, 'shorturl.at/girv9')
@bot.message_handler(commands=['email'])
def email(message):
      bot.reply_to(message, 'principal@iare.ac.in')
@bot.message_handler(commands=['brochure'])
def brochure(message):
      bot.send_document(message.chat.id,"https://www.iare.ac.in/IARE_2022-23_Brochure.pdf")
@bot.message_handler(commands=['cms'])
def cms(message):
      bot.reply_to(message,"Please visit this link")
      bot.send_message(message.chat.id,"samvidha.iare.ac.in")
@bot.message_handler(commands=['fee'])
def fee(message):
      bot.reply_to(message,"Please visit this website for fee structure")
      bot.send_message(message.chat.id,"https://iare.ac.in/?q=pages/fee-structure")
@bot.message_handler(commands=['appointment'])
def appointment(message):
      bot.reply_to(message,"To book appointment register in the fol    lowing link")
      bot.send_message(message.chat.id,"https://iare.ac.in/appointmentform.html")
@bot.message_handler(commands=['feedback'])
def feedback(message):
      bot.reply_to(message,"To give feedback visit the below link")
      bot.send_message(message.chat.id,"https://forms.gle/SUnTbpveWrMQvsEVA")
@bot.message_handler(commands=['phone'])
def phone(message):
      bot.send_message(message.chat.id,"Principal:040-29709851 or 9703618753\nDean of Planning\nMonitoring & Continuing Studies:9490244578\nDean of Academics:9703618749\nDean of Student Services:9966239198")
@bot.message_handler(commands=['qq'])
def qq(message):
      bot.send_document(message.chat.id,"https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/notification/2022-23/Deltax.pdf")



@bot.message_handler(content_types=['text'])
def context(message: Message):
      if "/" not in message.text:
            answer = ask(message.text)
            bot.reply_to(message, f"{str(answer)}")




bot.polling()