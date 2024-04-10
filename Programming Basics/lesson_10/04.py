from schema import session
from schema import Customer, Item, Order, OrderLine


o1 = Order(customer_id=1)

o2 = Order()
o2.customer_id = 1

line_item1 = OrderLine(order=o1, item_id=1, quantity=3)
line_item2 = OrderLine(order=o1, item_id=2, quantity=2)
line_item3 = OrderLine(order=o2, item_id=1, quantity=1)
line_item4 = OrderLine(order=o2, item_id=2, quantity=4)

session.add_all([o1, o2, line_item1, line_item2,
    line_item3, line_item4])

session.commit()
