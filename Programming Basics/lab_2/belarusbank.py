from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5 import uic
import sys
import requests


class Belarusbank(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []
        # загрузка файла
        uic.loadUi("branches.ui", self)
        # окно
        self.setWindowTitle("Branches")
        # вычисление
        self.pushButton.clicked.connect(self.get_filials_info)

    def get_filials_info(self):
        city = self.cityInput.toPlainText()
        print(city)
        # https://belarusbank.by/ru/33139/forDevelopers
        requests_string = f"https://belarusbank.by/open-banking/v1.0/banks/AKBBBY2X/branches"
        response = requests.get(requests_string)
        if response:
            print("Все ок:", response.content)
            self.answer = response.json()
            n = len(self.answer)
            self.filialsList.clear()
            print("Cleared")
            for i in range(n):
                if isinstance(self.answer[i], dict):
                    branch_info = QListWidgetItem(f"{self.answer[i]['filials_text']}\n")
                    self.filialsList.addItem(branch_info)
                else:
                    print("Error not dict")
        else:
            print("Что-то пошло не так.")
            print("Код ответа:", response.status_code)
            print("Причина:", response.reason)


app = QApplication([])
ex = Belarusbank()
ex.show()
app.exec()
