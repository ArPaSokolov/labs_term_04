from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("db_table_view.ui", self)
        self.pushButton.clicked.connect(self.press)

    def press(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('films_db.sqlite')
        db.open()

        model = QSqlQueryModel()
        query_string = """SELECT
        f.id,
        f.title AS [Название],
        g.title AS [Жанр],
        f.year AS [Год выпуска],
        f.duration AS [Длительность]
        FROM films f
        JOIN genres g ON f.genre = g.id"""
        model.setQuery(query_string, db)
        self.tableView.setModel(model)
        self.tableView.setColumnHidden(0, True)


app = QApplication([])
window = Form()
window.show()
app.exec()
