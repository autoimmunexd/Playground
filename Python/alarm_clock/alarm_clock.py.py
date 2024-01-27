#!/usr/bin/env python
import tkinter as tk
import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.time_var = tk.StringVar()
        self.date_var = tk.StringVar()
        tk.Label(self, textvariable=self.time_var).grid()
        tk.Label(self, textvariable=self.date_var).grid()

class AlarmClock:
    def __init__(self, time_var, date_var):
        self.time_var = time_var
        self.date_var = date_var
        self.update_display()

    def update_display(self):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%I:%M:%S %p")
        current_date = datetime.date.today()
        self.time_var.set(formatted_time) 
        self.date_var.set(current_date.strftime("%Y-%m-%d"))
        main_window.after(1000, self.update_display)

if __name__ == "__main__":
    main_window = Application()
    main_window.master.title("Alarm Clock")
    main_window.master.minsize(height=300, width=300)
    myclock = AlarmClock(main_window.time_var, main_window.date_var)
    main_window.mainloop()