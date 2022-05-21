from tkinter import *
from time import *
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
time= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time)
    canvas1.itemconfig(timer_text, text='00:00')
    label.config(text='Timer', fg=GREEN)
    label2.config(text='')
    global reps
    reps=0
    
    



# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps=0
def start_timer():
    global reps
    reps+=1

    work= WORK_MIN*60
    short= SHORT_BREAK_MIN*60
    long= LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long)
        label.config(text='Break', fg=RED)
    elif reps%2==0:
        count_down(short)
        label.config(text='Break', fg=PINK)
    else:
        count_down(work)
        label.config(text='Work', fg=GREEN)
        
        
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec=f'0{count_sec}'

    canvas1.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count>0:
        global time
        time= window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=''
        for _ in range(math.floor(reps/2)):
            marks += '✔'
        label2.config(text= marks)
        

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title('Pomodoro')
window.minsize(width=400, height=400)
window.config(padx=100, pady=50, bg=YELLOW)




bg= PhotoImage(file='./Udemy/PomodoroApp/tomato.png')
canvas1= Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas1.create_image(100,112, image= bg,)
timer_text= canvas1.create_text(100,138, text= '00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas1.grid(column=1, row=1)


label= Label(text= 'Timer', font=(FONT_NAME, 35, 'bold'), background=YELLOW, foreground=GREEN)
label.grid(column=1, row=0)
label2=Label( font=(FONT_NAME, 12, 'bold'), background=YELLOW, fg=GREEN)
label2.grid(column=1, row=3)

button_start= Button(window, text='Start', bd=5, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)
button_reset= Button(window, text='Reset', bd=5, highlightthickness=0, command= reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()