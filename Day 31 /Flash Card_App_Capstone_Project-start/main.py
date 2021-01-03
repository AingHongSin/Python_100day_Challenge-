from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')

word_dist = data.to_dict(orient = 'records')
current_word = {}

def next_word():
    global current_word, fliping_timer
    window.after_cancel(fliping_timer)
    current_word = random.choice(word_dist)
    canva_flash_card.itemconfig(title_card_label, text = 'French', fill = 'black')
    canva_flash_card.itemconfig(word_card_label, text = current_word['French'], fill = 'black')
    canva_flash_card.itemconfig(card_canvas, image = front_card_image)
    fliping_timer = window.after(3000, display_english_card)


def know_this_word():
    word_dist.remove(current_word)
    print(len(word_dist))
    new_data = pandas.DataFrame(word_dist)
    new_data.to_csv('./data/words_to_learn.csv', index = False)
    next_word()


def display_english_card():
    canva_flash_card.itemconfig(card_canvas, image = back_card_image)
    canva_flash_card.itemconfig(title_card_label, text = 'English', fill = 'white')
    canva_flash_card.itemconfig(word_card_label, text = current_word['English'], fill = 'white')

window = Tk()
window.title('Flashy')
window.config(background = BACKGROUND_COLOR)
window.config(padx = 50, pady = 50)

fliping_timer = window.after(3000, display_english_card)

front_card_image = PhotoImage(file = './images/card_front.png')
back_card_image = PhotoImage(file = './images/card_back.png')
right_image = PhotoImage(file = 'images/right.png')
wrong_image = PhotoImage(file = 'images/wrong.png')

canva_flash_card = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
card_canvas = canva_flash_card.create_image(403,267, image = front_card_image)
title_card_label = canva_flash_card.create_text(400, 150, text = 'Title', font = ('Ariel', 40, 'italic'))
word_card_label = canva_flash_card.create_text(400, 263, text = 'Word', font = ('Ariel', 60, 'italic'))
canva_flash_card.grid(row = 0, column = 0, columnspan = 2)

next_word()

wrong_button = Button(image = wrong_image, highlightthickness = 0, command = next_word())
wrong_button.grid(row = 1, column = 0)

right_button = Button(image = right_image, highlightthickness = 0, command = know_this_word)
right_button.grid(row = 1, column = 1)

window.mainloop()