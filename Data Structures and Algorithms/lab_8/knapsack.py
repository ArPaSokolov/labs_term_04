# Функция для нахождения максимальной ценности и элементов в рюкзаке
def knapsack(W, w, v, n):
    # двумерный массив для хранения оптимальных значений
    best = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Заполняем массив best по строкам и столбцам
    for i in range(n + 1):
        for j in range(W + 1):
            # Если i-й предмет не входит в рюкзак или его нет, то значение равно предыдущему
            if i == 0 or j == 0:
                best[i][j] = 0
            elif w[i - 1] <= j:
                # Если i-й предмет входит в рюкзак, то выбираем максимум из двух вариантов: взять его или не взять
                best[i][j] = max(v[i - 1] + best[i - 1][j - w[i - 1]], best[i - 1][j])
            else:
                # Если i-й предмет не входит в рюкзак, то значение равно предыдущему
                best[i][j] = best[i - 1][j]

    # Возвращаем максимальную ценность и элементы в рюкзаке
    value = best[n][W]  # Максимальная ценность
    items = []  # Список элементов в рюкзаке
    i = n  # Индекс последнего предмета
    j = W  # Оставшаяся вместимость рюкзака
    while i > 0 and j > 0:
        # Если значение в текущей ячейке отличается от предыдущего по строке, то i-й предмет был добавлен в рюкзак
        if best[i][j] != best[i - 1][j]:
            items.append(i)  # Добавляем индекс предмета в список
            j = j - w[i - 1]  # Уменьшаем оставшуюся вместимость на вес предмета
        i = i - 1  # Переходим к предыдущему предмету

    return value, items


# Дано
w = [10, 20, 30, 15, 20]  # Веса предметов
v = [60, 100, 120, 150, 349]  # Ценности предметов
W = 50  # Вместимость рюкзака

# Решение
n = len(w)  # Количество предметов
value, items = knapsack(W, w, v, n)

# Ответ
print("Максимальная ценность, которую можно уложить в рюкзак:", value)
print("Элементы в рюкзаке:", items)
