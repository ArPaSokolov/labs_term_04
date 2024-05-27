def firstFit(weight, n, c):
    # Инициализация результата (количество бинов)
    res = 0

    # Создайте массив для хранения
    # оставшееся пространство в бункерах
    # может быть не более n бинов
    bin_rem = [0] * n

    # Поместите элементы один за другим
    for i in range(n):

        # Найдите первую корзину, которая
        # может вместить
        # вес[i]
        j = 0

        # Инициализация минимального пространства
        # слева и индекс
        # наилучшего бина
        min = c + 1
        bi = 0

        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] -
                    weight[i] < min):
                bi = j
                min = bin_rem[j] - weight[i]

        # Если ни одна корзина не может вместить вес[i],
        # создайте новую корзину
        if (min == c + 1):
            bin_rem[res] = c - weight[i]
            res += 1
        else:  # Присвоить предмету лучшую корзину
            bin_rem[bi] -= weight[i]
    return res


if __name__ == '__main__':
    weight = [4, 4, 6, 6, 1, 8, 9, 1, 4, 2, 1]
    c = 10;
    n = len(weight);
    print("Количество необходимых ящиков: ",
          firstFit(weight, n, c));

