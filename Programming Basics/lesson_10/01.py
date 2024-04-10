from schema import session
from schema import Customer, Item, Order, OrderLine


c1 = Customer()
c1.first_name = 'Dmitriy'
c1.last_name = 'Yatsenko'
c1.username = 'Moseend'
c1.email = 'moseend@mail.com'

c2 = Customer(
    first_name='Valeriy', last_name='Golyshkin',
    username='Fortioneaks', email='fortioneaks@gmail.com'
)

print("Перед добавлением в сеанс:", c1, c2, sep="\n")

session.add(c1)
session.add(c2)
# Можно и так: session.add_all([c1, c2])

print("Перед отправкой в базу:", c1, c2, sep="\n")

session.commit()

print("После COMMIT:", c1, c2, sep="\n")
