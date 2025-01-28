# 7921307792: AAGieh1xu_qUwnTXKchlJHyQ59UTXUvQs-M
import requests
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from typing import Final
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters, ConversationHandler, ContextTypes, Application





# Replace with your API base URL and Telegram bot token
API_BASE_URL = "http://localhost:9000/store"  # Update with your API URL
TELEGRAM_BOT_TOKEN = "7921307792:AAGieh1xu_qUwnTXKchlJHyQ59UTXUvQs-M"
BOT_USERNAME: Final = "@store_sphere_bot"

# Conversation states
LOGIN_USERNAME, LOGIN_PASSWORD, ACTION = range(3)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome! Please log in to continue.\nSend your username:")
    return LOGIN_USERNAME

# Login: Username step


def login_username(update: Update, context: CallbackContext):
    context.user_data['username'] = update.message.text
    update.message.reply_text("Great! Now send your password:")
    return LOGIN_PASSWORD

# Login: Authenticate


def login_password(update: Update, context: CallbackContext):
    username = context.user_data['username']
    password = update.message.text

    # API login request
    login_url = "http://localhost:9000/auth/jwt/create"
    payload = {"username": username, "password": password}
    response = requests.post(login_url, data=payload)

    if response.status_code == 200:
        # Save JWT token
        # Assuming your API returns "access" for JWT token
        token = response.json().get("access")
        context.user_data['token'] = token
        update.message.reply_text(
            "Login successful! Choose an action:", reply_markup=main_menu())
        return ACTION
    else:
        update.message.reply_text(
            "Login failed. Please check your credentials and try again.")
        return LOGIN_USERNAME

