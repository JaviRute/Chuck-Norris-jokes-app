from tkinter import *
import requests
from googletrans import Translator

translator = Translator()

JOKE = ""
TRANSLATED = ""

def get_quote():
    global JOKE
    response = requests.get(url="https://api.chucknorris.io/jokes/random")
    response.raise_for_status()
    data = response.json()
    JOKE = data["value"]
    chuckanvas.itemconfig(quote_text, text=JOKE)

#Translate to each language
def translate_spanish():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="es")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_french():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="fr")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_greek():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="el")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_german():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="de")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_italian():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="it")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_portuguese():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="pt")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_chinese():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="zh-CN")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_japanese():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="ja")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_russian():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="ru")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_polish():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="pl")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_finnish():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="fi")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)

def translate_welsh():
    global JOKE
    global TRANSLATED
    TRANSLATED = translator.translate(JOKE, src="en", dest="cy")
    spanish_canvas.itemconfig(quote_spanish, text=TRANSLATED.text)


window = Tk()
window.title("NerdRage Apps - Chuck Norris joke translator...")
window.config(padx=50, pady=50, bg="#375362")

#Original joke canvass
chuckanvas = Canvas(width=300, height=414, bg="#375362", highlightthickness=0)
background_img = PhotoImage(file="images/background.png")
chuckanvas.create_image(150, 207, image=background_img)
quote_text = chuckanvas.create_text(150, 207, text="Chuck Norris can win the Nascar Tournament just turning right.", width=250, font=("Arial", 18, "bold"), fill="black")
chuckanvas.grid(row=0, column=0)

#Translated joke canvas
spanish_canvas = Canvas(width=300, height=414, bg="#375362", highlightthickness=0)
background_img_spanish = PhotoImage(file="images/background.png")
spanish_canvas.create_image(150, 207, image=background_img_spanish)
quote_spanish = spanish_canvas.create_text(150, 207, text="Choose language", width=250, font=("Arial", 18, "bold"), fill="black")
spanish_canvas.grid(row=0, column=1, columnspan=3)

#Chuck button
chuck_img = PhotoImage(file="images/chuck.png")
chuck_button = Button(image=chuck_img, highlightthickness=0, command=get_quote)
chuck_button.grid(row=1, column=0, rowspan=4)

#Other 9 buttons
spanish_img = PhotoImage(file="images/spanish_flag.png")
spanish_button = Button(image=spanish_img, highlightthickness=0, command=translate_spanish)
spanish_button.grid(row=1, column=1)

french_img = PhotoImage(file="images/french_flag.png")
french_button = Button(image=french_img, highlightthickness=0, command=translate_french)
french_button.grid(row=1, column=2)

greek_img = PhotoImage(file="images/greek_flag.png")
greek_button = Button(image=greek_img, highlightthickness=0, command=translate_greek)
greek_button.grid(row=2, column=3)

german_img = PhotoImage(file="images/german_flag.png")
german_button = Button(image=german_img, highlightthickness=0, command=translate_german)
german_button.grid(row=1, column=3)

italian_img = PhotoImage(file="images/italian_flag.png")
italian_button = Button(image=italian_img, highlightthickness=0, command=translate_italian)
italian_button.grid(row=2, column=1)

portuguese_img = PhotoImage(file="images/portuguese_flag.png")
portuguese_button = Button(image=portuguese_img, highlightthickness=0, command=translate_portuguese)
portuguese_button.grid(row=2, column=2)

chinese_img = PhotoImage(file="images/chinese_flag.png")
chinese_button = Button(image=chinese_img, highlightthickness=0, command=translate_chinese)
chinese_button.grid(row=3, column=1)

japanese_img = PhotoImage(file="images/japanese_flag.png")
japanese_button = Button(image=japanese_img, highlightthickness=0, command=translate_japanese)
japanese_button.grid(row=3, column=2)

russian_img = PhotoImage(file="images/russian_flag.png")
russian_button = Button(image=russian_img, highlightthickness=0, command=translate_russian)
russian_button.grid(row=3, column=3)

polish_img = PhotoImage(file="images/polish_flag.png")
polish_button = Button(image=polish_img, highlightthickness=0, command=translate_polish)
polish_button.grid(row=4, column=1)

finnish_img = PhotoImage(file="images/finnish_flag.png")
finnish_button = Button(image=finnish_img, highlightthickness=0, command=translate_finnish)
finnish_button.grid(row=4, column=2)

welsh_img = PhotoImage(file="images/welsh_flag.png")
welsh_button = Button(image=welsh_img, highlightthickness=0, command=translate_welsh)
welsh_button.grid(row=4, column=3)

get_quote()

window.mainloop()

