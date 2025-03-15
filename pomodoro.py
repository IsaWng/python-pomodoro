import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timer
    if timer is not None:
        window.after_cancel(timer)
        reps = 0
        canvas.itemconfig(timer_text, text="00:00")
        timer_label.config(text="Timer", fg=GREEN)
        label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count = LONG_BREAK_MIN
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count = SHORT_BREAK_MIN
    else:
        timer_label.config(text="Work", fg=GREEN)
        count = WORK_MIN
    count_down(count * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global reps
    hour = math.floor(seconds / 60)
    second = seconds % 60
    if second == 0:
        second = "00"
    elif second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{hour}:{second}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        done_sessions = math.floor(reps / 2)
        check_text = ""
        for n in range(done_sessions):
            check_text += "✔"
        label_check.config(text=check_text)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

image = PhotoImage(file="tomato.png")

canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness="0")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

button_start = Button()
button_start.config(text="Start", highlightthickness="0", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness="0", command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_check.grid(column=1, row=3)

window.mainloop()
