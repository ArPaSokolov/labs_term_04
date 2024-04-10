import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLabel


class Trick(QMainWindow):
    def __init__(self):
        super().init()
        self.setWindowTitle("List Widget Example")

if __name__ == "main":
    app = QApplication(sys.argv)
    window = Trick()
    window.show()
    sys.exit(app.exec_())