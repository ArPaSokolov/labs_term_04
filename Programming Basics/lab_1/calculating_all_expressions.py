from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []
        # загрузка файла
        uic.loadUi("calculating_all_expressions.ui", self)
        # окно
        self.setWindowTitle("Minicalculator")
        # вычисление
        self.pushButton.clicked.connect(self.calculating)

    def calculating(self):
        # получаем числа
        first_number = int(self.textEdit.toPlainText())
        second_number = int(self.textEdit_2.toPlainText())
        # считаем
        addition = first_number + second_number
        subtraction = first_number - second_number
        multiplication = first_number * second_number
        # проверка на дурака
        if second_number == 0:
            division = 'Error'
        else:
            division = first_number / second_number
        # выводим
        self.lcdNumber.display(str(addition))
        self.lcdNumber_2.display(str(subtraction))
        self.lcdNumber_3.display(str(multiplication))
        self.lcdNumber_4.display(str(division))


app = QApplication([])
ex = Calculator()
ex.show()
app.exec()
