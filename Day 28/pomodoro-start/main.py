from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repl = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    window.after_cancel(timer)
    canva.itemconfig(lbl_timertext, text = '00:00')
    lbl_Tick.config(text = "")
    lbl_Timer.config(text = 'Timer')

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repl
    repl += 1

    work_sec = WORK_MIN  * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repl % 8 == 0:
        lbl_Timer.config(text = 'Break', fg = RED)
        count_down(long_break_sec)
    elif repl % 2 == 0:
        lbl_Timer.config(text = 'Break', fg = PINK)

        count_down(short_break_sec)
    else:
        lbl_Timer.config(text = 'Work', fg = GREEN)

        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    canva.itemconfig(lbl_timertext, text = f"{str(count_min)}:{str(count_sec)}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repl/2)
        for _ in range(work_sessions):
            marks += '✓'
        lbl_Tick.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Tomato-Timer')
window.config(padx = 100, pady = 50, bg = YELLOW)

lbl_Timer = Label(text = 'Timer', font = (FONT_NAME, 48, 'bold'), bg = YELLOW, fg = GREEN)
lbl_Timer.grid(row = 0, column = 1)

canva = Canvas(width = 200, height = 223, bg = YELLOW, highlightthickness = 0)
Photo = PhotoImage(file = 'tomato.png')
canva.create_image(100, 110, image = Photo)
lbl_timertext = canva.create_text(100, 130, text = '00:00', font = (FONT_NAME, 35,'bold'), fill = 'white')
canva.grid(row = 1, column = 1)

btn_Start = Button(text = 'Start', width = 12, command = start_timer)
btn_Start.grid(row = 2, column = 0)

btn_Reset = Button(text = 'Reset', width = 12, command = timer_reset)
btn_Reset.grid(row = 2, column = 2)

lbl_Tick = Label(font = (FONT_NAME, 36), bg = YELLOW, fg = GREEN)
lbl_Tick.grid(row = 3, column = 1)

window.mainloop()