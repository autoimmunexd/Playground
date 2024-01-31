import eel
from alarm_clock import AlarmClock
#tells eel to use the folder named web
eel.init('web')
#creates our object out of alarmclock class
eel_clock = AlarmClock()
#starts the thread and it starts a funciton that contains a while loop that calls update time in infinite loop
eel_clock.tick_thread.start()
#creates the gui window using main.html
eel.start('main.html', size=(600,200))