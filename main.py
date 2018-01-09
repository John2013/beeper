import sys
from winsound import Beep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton)


class Example(QWidget):
    frequency = 37

    def __init__(self):
        super().__init__()

        self.initUI()

    def change(self, value):
        self.frequency = value

    def play(self):
        Beep(self.frequency, 100)

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.setMinimum(37)
        sld.setMaximum(32767)
        sld.setValue(37)

        playButton = QPushButton("Play", self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(playButton)

        self.setLayout(vbox)
        lcd.display(37)
        sld.valueChanged.connect(self.change)
        sld.valueChanged.connect(lcd.display)
        playButton.clicked.connect(self.play)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
