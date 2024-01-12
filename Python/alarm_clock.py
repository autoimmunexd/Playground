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
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        button = QPushButton("Eastern Time")
        button.setFixedSize(QSize(100, 100))
        self.setCentralWidget(button)

class AlarmClock:
    def __init__(self, time):
        _state = 'OFF'
        self.time = time

    def getCurrentTime(self, time):
        print(time)


        
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
    sys.exit(app.exec_())


#click button to set the current timezone
#current time
#alarm time
#remaining time until alarm
#sound options