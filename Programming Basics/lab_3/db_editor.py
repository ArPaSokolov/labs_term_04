import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QTableWidget, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt, pyqtSignal
import sqlite3


class FilmsTable(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []

        # загрузка файла
        uic.loadUi("db_viewer.ui", self)

        self.setWindowTitle("Фильмы")
        self.selected_row = None

        # таблица
        self.filmsTable.setColumnCount(5)
        self.filmsTable.setHorizontalHeaderLabels(["id", "Название", "Год выпуска", "Длительность", "Жанр"])
        self.filmsTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.filmsTable.doubleClicked.connect(self.edit_film)

        # подключение сигнала выбора строки к обработчику
        self.filmsTable.selectionModel().selectionChanged.connect(self.select_row)

        # кнопки
        self.addButton.clicked.connect(self.add_film)
        self.deleteButton.clicked.connect(self.delete_film)

        self.load_films()

    def load_films(self):
        # подключаемся к бд
        db_connection = sqlite3.connect("films_db.sqlite")
        cursor = db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS films \
                        (id INTEGER, title TEXT, year INTEGER, genre TEXT, duration INTEGER)")

        # получаем данные
        res = cursor.execute("SELECT * FROM films")
        films = res.fetchall()

        # запись в таблицу
        self.filmsTable.setRowCount(len(films))
        self.filmsTable.clearContents()

        for row, film in enumerate(films):
            for column, data in enumerate(film):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.filmsTable.setItem(row, column, item)

        # выравнивание столбцов по содержимому заголовков
        self.filmsTable.resizeColumnsToContents()

        # закрываем бд
        db_connection.close()

    def select_row(self, selected, deselected):
        indexes = selected.indexes()
        if indexes:
            selected_row = indexes[0].row()

            with sqlite3.connect("films_db.sqlite") as connection:
                curs = connection.cursor()
                curs.execute("SELECT id FROM films")
                rows = curs.fetchall()

            if rows:
                film_id = rows[selected_row][0]
                self.selected_row = film_id
            else:
                self.selected_row = None

    def edit_film(self, index):
        row = index.row()
        film_data = []

        for column in range(self.filmsTable.columnCount()):
            item = self.filmsTable.item(row, column)
            film_data.append(item.text())

        film_id = self.filmsTable.item(row, 0).text()
        editor = FilmsEditor(film_data, int(film_id))
        if editor.exec_() == QDialog.Accepted:
            self.load_films()

    def add_film(self):
        editor = FilmsEditor()
        if editor.exec() == QDialog.Accepted:
            title = editor.titleEdit.text()
            year = int(editor.yearEdit.text())
            genre = editor.genreEdit.text()
            duration = int(editor.durationEdit.text())

            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()
            # curs.execute("SELECT MAX(id) FROM films")
            print("!")

            # Определите SQL-запрос с использованием параметров для добавления новой строки в таблицу
            query_string = "INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)"
            curs.execute(query_string, (title, year, genre, duration))

            # Сохраните изменения в базе данных
            connection.commit()
            connection.close()

            # Загрузите обновленные данные из базы данных
            self.load_films()
            # self.close()

    def delete_film(self):
        selected_rows = [index.row() for index in self.filmsTable.selectedIndexes()]

        if len(selected_rows) > 0:
            # подтверждение
            reply = QMessageBox.question(self, "Подтверждение удаления",
                                         "Вы уверены, что хотите удалить выбранные фильмы?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                connection = sqlite3.connect("films_db.sqlite")
                curs = connection.cursor()

                film_id = self.selected_row  # Идентификатор фильма, который нужно удалить
                query_string = f"DELETE FROM films WHERE id = {film_id}"
                curs.execute(query_string)

                connection.commit()
                connection.close()
                # Загрузите обновленные данные из базы данных
                self.load_films()

class FilmsEditor(QDialog):
    def __init__(self, film_data=None, film_id=None):
        super().__init__()
        # загрузка файла
        uic.loadUi("film_edit.ui", self)

        self.setWindowTitle("Изменить")

        self.film_id = film_id
        if film_data:
            print(film_data)
            self.titleEdit.setText(film_data[1])
            self.yearEdit.setText(str(film_data[2]))
            self.genreEdit.setText(film_data[3])
            self.durationEdit.setText(str(film_data[4]))

        self.saveButton.clicked.connect(self.save_changes)

    def save_changes(self):
        title = self.titleEdit.text()
        year = int(self.yearEdit.text())
        genre = self.genreEdit.text()
        duration = int(self.durationEdit.text())

        if self.film_id is not None and self.film_id != 0:
            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()

            curs.execute("SELECT id FROM films")
            film_id = self.film_id
            query_string = f"UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?"
            curs.execute(query_string, (title, year, genre, duration, film_id))

            connection.commit()
            connection.close()
        else:
            connection = sqlite3.connect("films_db.sqlite")
            curs = connection.cursor()

            curs.execute("SELECT MAX(id) FROM films")
            max_id = curs.fetchone()[0]
            new_id = max_id + 1 if max_id is not None else 1

            # Определите SQL-запрос для добавления новой строки в таблицу
            query_string = "INSERT INTO films (id, title, year, genre, duration) VALUES (?, ?, ?, ?, ?)"

            curs.execute(query_string, (new_id, title, year, genre, duration))

            # Сохраните изменения в базе данных
            connection.commit()
            connection.close()

        self.accept()


app = QApplication([])
ex = FilmsTable()
ex.show()
app.exec()
