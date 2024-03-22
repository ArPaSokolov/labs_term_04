import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("db_table_widget.ui", self)
        self.pushButton.clicked.connect(self.press)

    def press(self):
        connection = sqlite3.connect("films_db.sqlite")
        curs = connection.cursor()
        query_string = '''SELECT
                            f.title AS [Название],
                            g.title AS [Жанр],
                            f.year AS [Год],
                            f.duration AS [Длительность]
                        FROM films f
                        JOIN genres g ON f.genre = g.id;'''
        result = curs.execute(query_string)
        captions = [t[0] for t in result.description]
        self.tableWidget.setColumnCount(len(captions))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(captions)

        for row in result:
            n = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(n + 1)
            k = len(row)
            for i in range(k):
                self.tableWidget.setItem(n, i, QTableWidgetItem(str(row[i])))

        connection.close()
        self.tableWidget.resizeColumnsToContents()


app = QApplication([])
window = Form()
window.show()
app.exec()
