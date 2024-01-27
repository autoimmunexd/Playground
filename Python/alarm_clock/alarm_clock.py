#!/usr/bin/env python
import datetime

class AlarmClock:
    def __init__(self):
        self.current_time = None
        self.current_date = None
        self.alarm_status = None
    
    def update_display(self):
            now = datetime.datetime.now()
            formatted_time = now.strftime("%I:%M:%S %p")
            current_date = datetime.date.today()
            self.current_time = formatted_time
            self.current_date = current_date
            self.alarm_status = None
            print(self.current_time)