# Добавим первых двух пользователей

from project_schema import factory
from project_schema import Student, Credit, Category


u3 = Student(last_name="Гвозденко", first_name="Демид", username="gvozdem", year="2", count_credit="30")
u4 = Student(last_name="Соколов", first_name="Арсений", username="sesha_xd", year="2", count_credit="35")
u1 = Student(last_name="Попов", first_name="Алексей", username="popiv", year="1", count_credit="5")
u2 = Student(last_name="Иванов", first_name="Иван", username="ivanovich", year="1", count_credit="59")
u5 = Student(last_name="Пупкин", first_name="Василий", username="pupok", year="3", count_credit="10")
u6 = Student(last_name="Шишкина", first_name="Анастасия", username="shishka", year="4", count_credit="0")

session = factory()
session.add_all([u1, u2, u3, u4, u5, u6])

names = ["Алгоритмы и структуры данных", "Дискретная математика", "Теория автоматов", "WEB", "Основы программирования"]
for s in names:
    c = Category()
    c.name = s
    session.add(c)
session.commit()

number = 10
st1 = Credit()
st1.title = "Сдано"
st1.content = f"{number} лабораторных"
c1 = session.query(Category).where(Category.name == "Алгоритмы и структуры данных").first()
st1.categories.append(c1)
st1.is_private = True
u1.credits.append(st1)
new_credit = u1.count_credit - number
if new_credit < 0:
    u1.count_credit = 0
else:
    u1.count_credit = f"{new_credit}"

number = 19
st2 = Credit()
st2.title = "Сдано"
st2.content = f"{number} лабораторных"
c2 = session.query(Category).where(Category.name == "WEB").first()
st2.categories.append(c2)
st2.is_private = True
u4.credits.append(st2)
new_credit = u4.count_credit - number
if new_credit < 0:
    u4.count_credit = 0
else:
    u4.count_credit = f"{new_credit}"

session.commit()
