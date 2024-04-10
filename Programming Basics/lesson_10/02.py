from schema import session
from schema import Customer, Item, Order, OrderLine


c3 = Customer(
    first_name = "Vadim", 
    last_name = "Moiseenko", 
    username = "Antence73", 
    email = "antence73@mail.com",
)

c4 = Customer(          
    first_name = "Vladimir", 
    last_name = "Belousov", 
    username = "Andescols", 
    email = "andescols@mail.com",       
)

c5 = Customer(
    first_name = "Tatyana", 
    last_name = "Khakimova", 
    username = "Caltin1962", 
    email = "caltin1962@mail.com",
)

c6 = Customer(
    first_name = "Pavel", 
    last_name = "Arnautov", 
    username = "Lablen", 
    email = "lablen@mail.com",
)

session.add_all([c3, c4, c5, c6])
session.commit()
