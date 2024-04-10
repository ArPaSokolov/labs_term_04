from schema import session
from schema import Customer, Item, Order, OrderLine


c1 = session.get(Customer, 1)
o1 = Order(customer=c1)

o2 = Order()
o2.customer = c1

i1 = session.get(Item, 1)
i2 = session.get(Item, 2)

detail1 = OrderLine()
detail1.order = o1
detail1.item = i1
detail1.quantity = 3

detail2 = OrderLine(order=o1, item=i2, quantity=2)

detail3 = OrderLine()
detail3.item = i1
detail3.quantity = 1

detail4 = OrderLine(item=i2, quantity=4)

o2.details.append(detail3)
o2.details.append(detail4)

session.add_all([o1, o2])

session.commit()
