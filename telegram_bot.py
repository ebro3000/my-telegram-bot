import os
from dotenv import load_dotenv
import telebot

# Load environment variables
load_dotenv()

# Get the bot token from the environment
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Define a command handler for /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to YourBot! Type /info to get more information.")

# Define a command handler for /info
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot implemented in Python.")

# Define a message handler to echo all messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.infinity_polling()
