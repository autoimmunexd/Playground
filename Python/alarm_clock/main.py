#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from alarm_clock import AlarmClock

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        # Create a Notebook to hold multiple tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, columnspan=3, rowspan=2)

        # Create the main clock tab
        self.clock_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.clock_tab, text='Clock')
        tk.Label(self.clock_tab, text="0:00xx").grid()

        # Create the settings tab
        # self.settings_tab = ttk.Frame(self.notebook)
        # self.notebook.add(self.settings_tab, text='Settings')
        # time_zone_combo = ttk.Combobox(
        #     self.settings_tab,
        #     state="readonly",
        #     values=["Eastern Standard Time", "Central Standard Time", "Mountain Standard Time", "Pacific Standard Time"]
        # )
        # time_zone_combo.grid()

if __name__ == "__main__":
    main_window = Application()
    main_window.master.title("Alarm Clock")
    main_window.master.minsize(height=300, width=300)
    main_window.mainloop()
    myclock = AlarmClock()
    myclock.update_display()



#settings tab
#select timezone
#alarm sound (youtube link) or select from current options


#current time
    