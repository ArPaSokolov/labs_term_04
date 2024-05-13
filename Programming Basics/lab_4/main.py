from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Film, Director, Actor, Base

# создаем соединение с базой данных SQLite
engine = create_engine('sqlite:///films.db')

# создаем таблицы в базе данных
Base.metadata.create_all(engine)

# создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# режиссеры
director1 = Director(name="Квентин Торантино")
director2 = Director(name="Мартин Скорсезе")

# фильмы
film1 = Film(title="Бесславные ублюдки", year=1994, director=director1)
film2 = Film(title="Однажды в... Голливуде", year=2019, director=director1)
film3 = Film(title="Волк с Уолл-стрит", year=2013, director=director2)

# актеры
actor1 = Actor(name="Леонардо Ди Каприо")
actor2 = Actor(name="Брэд Питт")
actor3 = Actor(name="Марго Робби")
actor4 = Actor(name="Кристоф Вальц")
actor5 = Actor(name="Мелани Лоран")
actor6 = Actor(name="Мэтью Макконахи")

# первый фильм
film1.actors.append(actor1)
film1.actors.append(actor2)
film1.actors.append(actor3)

# второй фильм
film2.actors.append(actor2)
film2.actors.append(actor3)
film2.actors.append(actor4)
film2.actors.append(actor5)

# третий фильм
film3.actors.append(actor1)
film3.actors.append(actor3)
film3.actors.append(actor6)

# добавляем данные в таблицу
session.add_all([director1, film1, film2, actor1, actor2, actor3, actor4, actor5])
session.commit()

# Получаем список всех фильмов из базы данных
films = session.query(Film).all()

# Выводим список фильмов, режиссеров и актеров
for film in films:
    print("Фильм:", film.title)
    print("Год:", film.year)
    print("Режиссер:", film.director.name)
    print("Актеры:")
    for actor in film.actors:
        print("- ", actor.name)
    print()
