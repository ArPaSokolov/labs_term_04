from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5 import uic


class Order(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []
        # загрузка файла
        uic.loadUi("cheque.ui", self)
        # окно
        self.setWindowTitle("Order in Vkysno i tochka")
        # вычисление
        self.pushButton.clicked.connect(self.cheque)

    def cheque(self):
        text = str()
        if self.checkBox.isChecked():
            text += "- Чизбургер\n"
        if self.checkBox_2.isChecked():
            text += "- Мороженка\n"
        if self.checkBox_3.isChecked():
            text += "- Добрый кола\n"
        if self.checkBox_4.isChecked():
            text += "- Нагетсы\n"
        if text != "":
            self.textEdit.setText(text)


app = QApplication([])
ex = Order()
ex.show()
app.exec()
