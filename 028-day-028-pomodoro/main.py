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
CHECK_MARK = "✔"
reps = 0
timer = None
check_mark_str = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, check_mark_str, reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark_str = None
    check_label.config(text=check_mark_str)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    if reps in (1, 3, 5, 7):
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    if reps in (2, 4, 6):
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    if reps == 8:
        reps = 0
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check_mark_str, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0:
            check_mark_str += CHECK_MARK
            check_label.config(text=check_mark_str)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Column 1
start_btn = Button(text="Start", command=start)
start_btn.grid(column=1, row=3)

# Column 2
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=1)

tomato_img = PhotoImage(file="./tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)

check_mark_str = None
check_label = Label(
    text=check_mark_str, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal")
)
check_label.grid(column=2, row=4)

# Column 3
reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=3, row=3)


window.mainloop()
