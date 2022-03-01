# First see Readme file!
import time as tme
from tkinter import *




clock = Tk()
none = 1
clock.configure(background='black')
ctime = tme.strftime("%I:%M:%S %p")
time = Label(font=("ds-digital", 200), bg="black", fg="green")
clock.title("Clock")
clock.geometry("1300x200")
time.pack()
def digitalclock():
    text_input = tme.strftime("%I:%M:%S %p")
    time.config(text=text_input)
    time.after(200, digitalclock)
digitalclock()
clock.mainloop()
