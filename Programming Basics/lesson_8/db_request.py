import sqlite3

x = int(input("Введите год выпуска фильма: "))

connection = sqlite3.connect("films_db.sqlite")
curs = connection.cursor()

query_string = f"SELECT * FROM films WHERE year = {x}"
result = curs.execute(query_string)
# A = result.fetchall()
#        ||
# A = list(result)
# print(type(A))

# print(result.descriptions)

captions = [t[0] for t in result.description]
print(*captions)

count = 0
for row in result:
    count += 1
    print(*row)
print(f"Найдено {count} результатов поиска")

connection.close()
