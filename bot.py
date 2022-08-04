from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

sur = requests.get('https://sinoptik.ua/погода-денау')
html_sur = BS(sur.content, 'html.parser')
####################################################
tosh = requests.get('https://sinoptik.ua/погода-ташкент')
html_tosh = BS(tosh.content, 'html.parser')
###################################################
far = requests.get('https://sinoptik.ua/погода-фергана')
html_far = BS(far.content, 'html.parser')
####################################################
qash = requests.get('https://sinoptik.ua/погода-шахрисабз')
html_qash = BS(qash.content, 'html.parser')
####################################################
bux = requests.get('https://sinoptik.ua/погода-бухара')
html_bux = BS(bux.content, 'html.parser')
####################################################
sam = requests.get('https://sinoptik.ua/погода-самарканд')
html_sam = BS(sam.content, 'html.parser')
####################################################
qor = requests.get('https://sinoptik.ua/погода-нукус')
html_qor = BS(qor.content, 'html.parser')
####################################################
andj = requests.get('https://sinoptik.ua/погода-андижан')
html_andj = BS(andj.content, 'html.parser')
####################################################
jiz = requests.get('https://sinoptik.ua/погода-джизак')
html_jiz = BS(jiz.content, 'html.parser')
####################################################
xor = requests.get('https://sinoptik.ua/погода-хива')
html_xor = BS(xor.content, 'html.parser')
####################################################
nam = requests.get('https://sinoptik.ua/погода-наманган')
html_nam = BS(nam.content, 'html.parser')
####################################################
nav = requests.get('https://sinoptik.ua/погода-навои')
html_nav = BS(nav.content, 'html.parser')




for el in html_tosh.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    tosh_min = min[4:]
    tosh_max = max[5:]
    print(tosh_min, tosh_max)
###################################################
for el in html_sur.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    sur_min = min[4:]
    sur_max = max[5:]
    print(sur_min, sur_max)
###################################################
for el in html_far.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    far_min = min[4:]
    far_max = max[5:]
    print(far_min, far_max)
####################################################
for el in html_qash.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    qash_min = min[4:]
    qash_max = max[5:]
    print(qash_min, qash_max)
####################################################
for el in html_bux.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    bux_min = min[4:]
    bux_max = max[5:]
    print(bux_min, bux_max)
####################################################
for el in html_sam.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    sam_min = min[4:]
    sam_max = max[5:]
    print(sam_min, sam_max)
####################################################
for el in html_qor.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    qor_min = min[4:]
    qor_max = max[5:]
    print(qor_min, qor_max)
####################################################
for el in html_andj.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    andj_min = min[4:]
    andj_max = max[5:]
    print(andj_min, andj_max)
####################################################
for el in html_jiz.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    jiz_min = min[4:]
    jiz_max = max[5:]
    print(jiz_min, jiz_max)
####################################################
for el in html_xor.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    xor_min = min[4:]
    xor_max = max[5:]
    print(xor_min, xor_max)
####################################################
for el in html_nam.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    nam_min = min[4:]
    nam_max = max[5:]
    print(nam_min, nam_max)
####################################################
for el in html_nav.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    nav_min = min[4:]
    nav_max = max[5:]
    print(nav_min, nav_max)
####################################################


def city():
    return [
        [InlineKeyboardButton("Denov", callback_data=f"01")],
        #######################################################
        [InlineKeyboardButton("Toshkent", callback_data=f"02")],
        ######################################################
        [InlineKeyboardButton("Farg`ona", callback_data=f"03")],
        #######################################################
        [InlineKeyboardButton("Qarqadaryo", callback_data=f"04")],
        #######################################################
        [InlineKeyboardButton("Buxoro", callback_data=f"05")],
        #######################################################
        [InlineKeyboardButton("Samarqand", callback_data=f"06")],
        #######################################################
        [InlineKeyboardButton("Qoraqalpog`iston", callback_data=f"07")],
        #######################################################
        [InlineKeyboardButton("Andjon", callback_data=f"08")],
        #######################################################
        [InlineKeyboardButton("Jizzax", callback_data=f"09")],
        #######################################################
        [InlineKeyboardButton("Xorazm", callback_data=f"10")],
        #######################################################
        [InlineKeyboardButton("Namangan", callback_data=f"11")],
        #######################################################
        [InlineKeyboardButton("Navoi", callback_data=f"12")],
        #######################################################
    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back2():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back3():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back4():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back5():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back6():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back7():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back8():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back9():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back10():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back11():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]
#########################################
def back12():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
   ]
########################################


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Bugun Denov shaxrida havo o`zgarib turadi\nmin {sur_min}\nmax "
                                f"{sur_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "02":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {tosh_min}\nmax "
                                f"{tosh_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
       
    elif data[0] == "03":
        query.message.edit_text(f"Bugun Farg`ona shaxrida havo o`zgarib turadi\nmin {far_min}\nmax "
                                f"{tosh_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "04":
        query.message.edit_text(f"Bugun Qashqadaryo  shaxrida havo o`zgarib turadi\nmin {qash_min}\nmax "
                                f"{qash_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "05":
        query.message.edit_text(f"Bugun Buxoro shaxrida havo o`zgarib turadi\nmin {bux_min}\nmax "
                                f"{bux_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "06":
        query.message.edit_text(f"Bugun Samarqand shaxrida havo o`zgarib turadi\nmin {sam_min}\nmax "
                                f"{sam_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "07":
        query.message.edit_text(f"Bugun Qoraqalpog`iston shaxrida havo o`zgarib turadi\nmin {qor_min}\nmax "
                                f"{qor_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "08":
        query.message.edit_text(f"Bugun Andijon Respublikasida havo o`zgarib turadi\nmin {andj_min}\nmax "
                                f"{andj_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "09":
        query.message.edit_text(f"Bugun Jizzax shaxrida havo o`zgarib turadi\nmin {jiz_min}\nmax "
                                f"{jiz_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "010":
        query.message.edit_text(f"Bugun xorazm shaxrida havo o`zgarib turadi\nmin {xor_min}\nmax "
                                f"{xor_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "11":
        query.message.edit_text(f"Bugun Namangan shaxrida havo o`zgarib turadi\nmin {nam_min}\nmax "
                                f"{nam_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))

    elif data[0] == "12":
        query.message.edit_text(f"Bugun Navoi shaxrida havo o`zgarib turadi\nmin {nav_min}\nmax "
                                f"{nav_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "TOKEN o'zingizni tokeningizni qoying"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Davomini o`zingiz mustaqil bajaring!!!











