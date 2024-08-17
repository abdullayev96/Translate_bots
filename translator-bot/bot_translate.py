# from googletrans import Translator
#
# tr = Translator()
# from telegram import KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import globals
# from database import Database
# from datetime import datetime
#
# TOKEN=""
#
# database = Database("member.db")
#
#
# def start_command(update, context):
#     user_id = update.message.from_user.id
#     username = update.message.from_user.username
#     user = database.get_user_by_chat_id(user_id)
#     if not user:
#         database.create_user(user_id, username, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
#     button = [
#         [KeyboardButton(globals.language[1]), KeyboardButton(globals.language[2])],
#         [KeyboardButton(globals.language[3]), KeyboardButton(globals.language[4])],
#         [KeyboardButton(globals.language[5]), KeyboardButton(globals.language[6])]
#     ]
#     update.message.reply_html(
#         "<b>Quydagilardan birini tanlang\n\nВыберите один из следующих\n\nChoose one of the following</b>\n\n🔽🔽🔽🔽🔽🔽",
#         reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True))
#
#
# def user_command(update, context):
#     users = database.count_user()
#     count = 0
#     for user in users:
#         count += 1
#     update.message.reply_html(
#         text=f"<b>Foydalanuvchilar soni</b> {count}\n\n<b>Количество пользователей</b> {count}\n\n<b>Quantity of users</b> {count}")
#
# def help_command(update,context):
#     update.message.reply_text(text=f"{globals.helpp[1]}\n\n{globals.helpp[2]}\n\n{globals.helpp[3]}")
#
# def message_handler(update, context):
#     state = context.user_data.get('state', 0)
#     msg = update.message.text
#     if msg == globals.language[1] or msg == globals.language[3]:
#         update.message.reply_html("matn kiriting:")
#
#         if msg == globals.language[1]:
#             context.user_data['state'] = 1
#         else:
#             context.user_data['state'] = 3
#
#     elif msg == globals.language[2] or msg == globals.language[5]:
#         update.message.reply_html("введите текст:")
#         if msg == globals.language[2]:
#             context.user_data['state'] = 2
#         else:
#             context.user_data['state'] = 5
#
#     elif msg == globals.language[4] or msg == globals.language[6]:
#         update.message.reply_html("enter the text:")
#         if msg == globals.language[4]:
#             context.user_data['state'] = 4
#         else:
#             context.user_data['state'] = 6
#     elif state == 1:
#         result = tr.translate(msg, src='uz', dest='ru')
#         update.message.reply_text(f"{result.text}")
#     elif state == 2:
#         result = tr.translate(msg, src='ru', dest='uz')
#         update.message.reply_text(f"{result.text}")
#     elif state == 3:
#         result = tr.translate(msg, src='uz', dest='en')
#         update.message.reply_text(f"{result.text}")
#     elif state == 4:
#         result = tr.translate(msg, src='en', dest='uz')
#         update.message.reply_text(f"{result.text}")
#     elif state == 5:
#         result = tr.translate(msg, src='ru', dest='en')
#         update.message.reply_text(f"{result.text}")
#     elif state == 6:
#         result = tr.translate(msg, src='en', dest='ru')
#         update.message.reply_text(f"{result.text}")
#     else:
#         start_command(update,context)
#
#
# updater = Updater(TOKEN, use_context=True)
# dispatcher = updater.dispatcher
#
# dispatcher.add_handler(CommandHandler("start", start_command))
# dispatcher.add_handler(CommandHandler("users", user_command))
# dispatcher.add_handler(CommandHandler("help", help_command))
# dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
# updater.start_polling()
# updater.idle()


from googletrans import Translator
from deep_translator import GoogleTranslator
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import globals
from database import Database
from datetime import datetime

TOKEN=""

database = Database("member.db")

def start_command(update, context):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    user = database.get_user_by_chat_id(user_id)
    if not user:
        database.create_user(user_id, username, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    button = [
        [KeyboardButton(globals.language[1]), KeyboardButton(globals.language[2])],
        [KeyboardButton(globals.language[3]), KeyboardButton(globals.language[4])],
        [KeyboardButton(globals.language[5]), KeyboardButton(globals.language[6])],
        [KeyboardButton(globals.language[7]), KeyboardButton(globals.language[8])],
        [KeyboardButton(globals.language[9]), KeyboardButton(globals.language[10])]
    ]


    update.message.reply_html(
        "<b>Quydagilardan birini tanlang\n\nВыберите один из следующих\n\nChoose one of the following</b>\n\n اختر واحدة أدناه \n\n 🔽🔽🔽🔽🔽🔽",
        reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True))


def user_command(update, context):
    users = database.count_user()
    count = 0
    for user in users:
        count += 1
    update.message.reply_html(
        text=f"<b>Foydalanuvchilar soni</b> {count}\n\n<b>Количество пользователей</b> {count}\n\n<b>Quantity of users</b> {count}")



def help_command(update,context):
    update.message.reply_text(text=f"{globals.helpp[1]}\n\n{globals.helpp[2]}\n\n{globals.helpp[3]}\n\n{globals.helpp[4]}")



def translate_text(text, src, dest):
    return GoogleTranslator(source=src, target=dest).translate(text)





def message_handler(update, context):
    state = context.user_data.get('state', 0)
    msg = update.message.text

####  uz

    if msg == globals.language[1] or msg == globals.language[3] or msg == globals.language[9]:
        update.message.reply_html("matn kiriting:")
        if msg == globals.language[1]:
            context.user_data['state'] = 1

        elif msg == globals.language[3]:
            context.user_data['state'] = 3
        else:
            context.user_data['state'] = 9

#### ru
    elif msg == globals.language[2] or msg == globals.language[5]:
        update.message.reply_html("введите текст:")
        if msg == globals.language[2]:
            context.user_data['state'] = 2
        else:
            context.user_data['state'] = 5

#### en

    elif msg == globals.language[4] or msg == globals.language[6] or msg == globals.language[10]:
        update.message.reply_html("enter the text:")
        if msg == globals.language[4]:
            context.user_data['state'] = 4

        elif msg == globals.language[6]:
            context.user_data['state'] = 6

        else:
            context.user_data['state'] = 10

### ar

    elif msg == globals.language[7] or msg == globals.language[8]:
        update.message.reply_html("أدخل النص:")
        if msg == globals.language[7]:
            context.user_data['state'] = 7
        else:
            context.user_data['state'] = 8

    else:
        try:
            if state == 1:
                result = translate_text(msg, 'uz', 'ru')
                update.message.reply_text(f"{result}")

            elif state == 2:
                result = translate_text(msg, 'ru', 'uz')
                update.message.reply_text(f"{result}")

            elif state == 3:
                result = translate_text(msg, 'uz', 'en')
                update.message.reply_text(f"{result}")

            elif state == 4:
                result = translate_text(msg, 'en', 'uz')
                update.message.reply_text(f"{result}")

            elif state == 5:
                result = translate_text(msg, 'ru', 'en')
                update.message.reply_text(f"{result}")

            elif state == 6:
                result = translate_text(msg, 'en', 'ru')
                update.message.reply_text(f"{result}")

            elif state == 7:
                result = translate_text(msg, 'ar', 'en')
                update.message.reply_text(f"{result}")

            elif state == 8:
                result = translate_text(msg, 'ar', 'uz')
                update.message.reply_text(f"{result}")

            elif state == 9:
                result = translate_text(msg, 'uz', 'ar')
                update.message.reply_text(f"{result}")

            elif state == 10:
                result = translate_text(msg, 'en', 'ar')
                update.message.reply_text(f"{result}")



        except Exception as e:
            update.message.reply_text("Translation service is currently unavailable. Please try again later.")
        start_command(update, context)


updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("users", user_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
updater.idle()




