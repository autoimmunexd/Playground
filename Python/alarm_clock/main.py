import eel
from alarm_clock import AlarmClock

# Tells eel to use the folder named web
eel.init('web')

# Creates our object out of the AlarmClock class
eel_clock = AlarmClock()

# Starts the thread that contains a while loop calling update_time
eel_clock.tick_thread.start()

# Creates the GUI window using main.html
chrome_flags = [
    '--window-size=800,600',
    '--app',
    '--disable-frame-rate-limit',
    '--disable-gpu',
    '--disable-canvas-aa',
]

# Start the Eel app with the specified options
eel.start('main.html', mode='chrome', size=(520, 500), chromeFlags=chrome_flags, suppress_error=True)