import tkinter
from tkinter import messagebox
import time
import threading
from PIL import Image, ImageTk
from game_engine import GameEngine

#_________________________________________Initialization of Objects____________________________________________#

window = tkinter.Tk()
window.title("Lightning Typing Test")
window.minsize(width=350, height=500)

game_engine = GameEngine()
secs_left = 60
#_______________________________________________Constants________________________________________________________#


#__________________________________________Definition of Functions_______________________________________________#

def gen_new_test():
    global secs_left
    random_text = game_engine.get_text()
    text_canvas = tkinter.Canvas(width=350, height=220, bg="#b1b4ba")
    text_canvas.create_text(175, 110, text=random_text, fill="black", font=('Arial', 10, 'normal'), width=340)
    text_canvas.grid(row=3, column=0, columnspan=2)
    if secs_left <= 0:
        secs_left = 60
    canvas.itemconfig(timer_text, text="60")
    start_btn.configure(state="active")
    entry_box.configure(state="normal")
    entry_box.delete(0, "end")


def update_countdown():
    global secs_left
    if secs_left >= 0:
        canvas.itemconfig(timer_text, text=str(secs_left))
        secs_left -= 1
        window.after(1000, update_countdown)
    else:
        new_test_button.configure(state='active')
        result_btn.configure(state="active")
        entry_box.configure(state="disabled")


def start_test():
    global secs_left
    secs_left = 60
    entry_box.delete(0, "end")
    start_btn.configure(state="disabled")
    new_test_button.configure(state='disabled')
    result_btn.configure(state="disabled")
    update_countdown()


def check_result():
    score = game_engine.calculate_score(entry_box.get())
    print(score)
    tkinter.messagebox.showinfo("Your score", f"Your score is: {score}" )



#______________________________________Window Title / Clock Display_______________________________________________#

heading_label = tkinter.Label(text="Lightning Typing Test")
heading_label.config(font=('Georgia', 30, 'bold'))
heading_label.grid(row=0, column=0, columnspan=2)

square = Image.open("rounded square.png")
resized_square = square.resize((150, 150))
tk_oval = ImageTk.PhotoImage(resized_square)
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=tk_oval)
timer_text = canvas.create_text(100, 85, text="60", fill="white", font=('Arial', 50, 'bold'))
seconds_text = canvas.create_text(100, 135, text="seconds", fill="white", font=('Arial', 20, 'bold'))
canvas.grid(row=1, column=0, columnspan=2)

new_test_button = tkinter.Button(text="New Test", command=gen_new_test)
new_test_button.config(font=('Georgia', 10, 'normal'))
new_test_button.grid(row=2, column=0, columnspan=2)

text_canvas = tkinter.Canvas(width=350, height=220, bg="#b1b4ba")
text_display = text_canvas.create_text(175, 100, text="Press the 'New Test' button to start", fill="black", font=('Arial', 10, 'normal'), width=340)
text_canvas.grid(row=3, column=0, columnspan=2)


entry_box = tkinter.Entry(width=60)
entry_box.configure(state="disabled")
entry_box.grid(row=4, column=0, columnspan=2, pady=10)

start_btn = tkinter.Button(text="Start Test", command=start_test)
start_btn.config(font=('Georgia', 10, 'normal'))
start_btn.grid(row=5, column=0, sticky="E")

result_btn = tkinter.Button(text="Check Result", command=check_result)
result_btn.config(font=('Georgia', 10, 'normal'))
result_btn.grid(row=5, column=1, sticky='W')


window.mainloop()