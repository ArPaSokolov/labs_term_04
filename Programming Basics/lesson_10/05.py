from schema import session
from schema import Customer, Item, Order, OrderLine

result = session.query(Customer).filter(Customer.last_name.like("%ko"))

for x in result:
    print(x)

# c = Customer()
# c.first_name = "Олег"
# c.last_name = "Полковский"
# c.email = "polkovsky@mail.ru"
# c.username = "MegaStar025"
#
# session.add(c)
#
# try:
#     session.commit()
#     print("Пользователь успешно создан")
# except Exception as e:
#     print("Не удалось добавить пользователя:", e)
#     session.rollback()
