import math


def calculate_G(a, x, f_x):
    if a * x > 0:
        return math.sin(f_x + a) ** 2 - math.sqrt(abs(f_x))
    elif a * x < 0:
        return (f_x + 2 * a) ** 2 - math.sqrt(abs(f_x))
    else:
        return (f_x + 2 * a) ** 2 + 1


a = int(input("Введите значение параметра a: "))
choice = input("Выберите функцию f(x) (ex или x2): ")

print("|  a  |  x  |  f(x)  |  G(x)  |")
print("-----------------------------")

if choice == "ex":
    for x in range(-5, 6):
        f_x = math.exp(x)
        g_x = calculate_G(a, x, f_x)
        print(f"| {a} | {x}  |  {f_x:.2f}  |  {g_x:.2f}  |")

elif choice == "x2":
    for x in range(-5, 6):
        f_x = x ** 2
        g_x = calculate_G(a, x, f_x)
        print(f"| {a} | {x}  |  {f_x}  |  {g_x:.2f}  |")

else:
    print("Некорректный выбор функции f(x).")
