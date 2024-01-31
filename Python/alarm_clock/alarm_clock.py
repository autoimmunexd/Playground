from datetime import datetime
import time
import os.path
import configparser
import threading
import eel

config = configparser.ConfigParser()


class AlarmClock:
    def __init__(self):
        # binds the thread to the specific instance of the class.  targets the tick() method and runs it in a seperate thread to stop blocking
        self.tick_thread = threading.Thread(target=self.tick)
        # if the config file exists
        if os.path.isfile('config.ini'):
            # open the config file and set to variable configfile
            with open('config.ini', 'r') as configfile:
                # read() the config file
                configfile.read()
        else:
            # if the config file doesn't exist, make one that looks like this with default values
            config['Clock'] = {
                'alarm_state': '',
                'alarm_time': '',
                'alarm_sound': ''
            }  # create a config.ini file
            with open('config.ini', 'w') as configfile:
                # write the config ini file with the config default values
                config.write(configfile)
        # clock is running init method so set the current time to the current time
        self.current_time = time.strftime("%I:%M %p")
        self.seconds = None
        # set am_pm
        self.am_pm = None
        # set alarm_state
        self.alarm_state = None
        # decides if it's morning or night based off the array index of 1 after splitting at the space in the returned string from current_time
        if self.current_time.split(' ')[1] == 'AM':
            self.am_pm = 'AM'
        else:
            self.am_pm = 'PM'

        # decorate to add functionality to the eel class with our update time method

    @eel.expose
    # update time method calls the javascript function and passes in a value of another
    # function that returns the current time of the instance of the alarmclock class
    def update_time_ui(self, time, seconds):
        eel.updateTime(time, seconds)

    def update_time(self):
         # Get the current time
         current_timex = datetime.now().time()
         # Extract the seconds from the current time
         self.seconds = current_timex.second
         self.current_time = time.strftime("%I:%M %p")
         self.update_time_ui(self.current_time, self.seconds)

    def tick(self):
        while True:
            self.update_time()
            time.sleep(1)
            print('tik')

# if __name__ == '__main__':
#     print(' hello world!')
#     myclock = AlarmClock()


# value = config.get('section_name', 'key_name')
# print(value)