import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import pytz
from datetime import datetime

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto's Alarm")
        self.setGeometry(100, 100, 300, 150)
        button = QPushButton("Eastern Time")
        button.setFixedSize(QSize(100, 100))
        self.setCentralWidget(button)

class AlarmClock:
    def __init__(self):
        self.state = 'OFF'
        self.time = datetime.now()

    def getCurrentTime(self):
        #converts the datetime.now() to a 12 hour readable format.
        print(self.time.strftime("%I:%M:%S%p"))

    def getState(self):
        if self.state == 'OFF':
            print('The alarm is off.')
        else:
            print('The alarm is on.')


    #working on this part right here, printing the current time to a label
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.update_time)
    #     self.timer.start(1000)  # 1000 milliseconds = 1 second
    #     # Initial update
    #     self.update_time()

    # def update_time(self):
    #     current_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    #     self.time_label.setText(current_time)


#settings management with json
#         import json

# # Writing settings to a file
# settings = {'variable1': 'value1', 'variable2': 'value2'}
# with open('config.json', 'w') as jsonfile:
#     json.dump(settings, jsonfile)

# # Reading settings from a file
# with open('config.json', 'r') as jsonfile:
#     loaded_settings = json.load(jsonfile)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    clock = AlarmClock()
    clock.getState()
    clock.getCurrentTime()
    sys.exit(app.exec_())

#click button to set the current timezone
#current time
#alarm time
#remaining time until alarm
#sound options