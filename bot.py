from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

TOKEN = 'BOT_TOKEN'
updater = Updater(TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the TEC ROOM Info Bot. Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
/about - About TEC ROOM
/website - To get the Website URL
/facebook - To get the Facebook page URL
/youtube - To get the YouTube channel URL
/instagram - To get the Instagram profile URL
/linkedin - To get the LinkedIn URL
/twitter - To get the Twitter URL
/tiktok - To get the TikTok URL
/pinterest - To get the Pinterest URL
/telegram - To get the Telegram URL""")

def about_txt(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM  is a Sri Lankan technology website, publishing news, feature stories, software & app reviews, tech tutorials and product reviews in Sinhala. The main purpose of the website is to bring the latest tech news, tech tutorials in the Sinhala language and respect user contributions by letting anyone contribute and update the latest news, In the same manner, anyone with access to the website can read news and get the latest updates via the official website. ")

def website_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Website URL => https://tecroom.lk")

def facebook_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Facebook Page Link => https://www.facebook.com/tecroompage")

def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM YouTube Channel Link => https://www.youtube.com/tecroom")

def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Instagram Link => https://www.instagram.com/tecroom.official")

def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM LinkedIn URL => https://linkedin.com/company/tecroom")

def twitter_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Twitter Link => https://twitter.com/tecroom")

def tiktok_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM TikTok Link => https://tiktok.com/@tecroom.official")

def pinterest_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Pinterest Link => https://www.pinterest.com/tecroom")

def telegram_url(update: Update, context: CallbackContext):
    update.message.reply_text("TEC ROOM Telegram Channel Link => https://t.me/tecroom_official")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('about', about_txt))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('facebook', facebook_url))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter_url))
updater.dispatcher.add_handler(CommandHandler('tiktok', tiktok_url))
updater.dispatcher.add_handler(CommandHandler('pinterest', pinterest_url))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
