from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Trick(QMainWindow):
    def __init__(self):
        super().__init__()
        self.children = []
        # загрузка файла
        uic.loadUi("word_shifter.ui", self)
        # окно
        self.setWindowTitle("Trick")
        # кнопка
        self.pushButton.setText("->")
        # фокус
        self.pushButton.clicked.connect(self.word_shifter)

    def word_shifter(self):
        if self.pushButton.text() == "->":
            word = self.textEdit.toPlainText()
            self.textEdit2.setText(word)
            self.pushButton.setText("<-")
            self.textEdit.setText("")

        elif self.pushButton.text() == "<-":
            word = self.textEdit2.toPlainText()
            self.textEdit.setText(word)
            self.pushButton.setText("->")
            self.textEdit2.setText("")


app = QApplication([])
ex = Trick()
ex.show()
app.exec()
