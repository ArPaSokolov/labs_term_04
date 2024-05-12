from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []
        # загрузка файла
        uic.loadUi("calculating_expressions.ui", self)
        # окно
        self.setWindowTitle("calculating expressions")
        # кнопка
        self.pushButton.setText("=")
        # вычисление
        self.pushButton.clicked.connect(self.calculating)

    def calculating(self):
        expression = self.textEdit.toPlainText()
        try:
            result = eval(expression)
            self.textEdit2.setText(str(result))
        # проверка на дурака
        except Exception as e:
            self.textEdit2.setText("Error: " + str(e))


app = QApplication([])
ex = Calculator()
ex.show()
app.exec()
