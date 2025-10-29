from tkinter import *
from time import strftime

class DigitalClock:
    def __init__(self,window):
        self.window = window
        self.window.title("Digital Clock")

        self.label = Label(self.window, font=("calibri", 50, "bold"), background="yellow", foreground="black")
        self.label.pack(anchor="center")

        self.time()

    def time(self):
        time_string = strftime("%H:%M:%S %p \n %D")
        self.label.config(text=time_string)
        self.label.after(1000,self.time)

if __name__ == "__main__":
    window_object = Tk()
    clock_object = DigitalClock(window_object)
    window_object.mainloop()







