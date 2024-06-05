def first_fit(weights, capacity):
    # минимальное необходимых количество корзин
    res = 0

    # массив для хранения оставшегося места в корзинах
    bin_rem = [0]

    # идем по весам предметов
    for weight in weights:
        min_remainder = capacity + 1  # минимальная вместимость
        best_bin = 0

        # идем по имеющимся корзинам
        for j in range(res):
            # место нашлось и оно наименьшее
            if bin_rem[j] >= weight and bin_rem[j] - weight < min_remainder:
                best_bin = j  # запоминаем номер корзины
                min_remainder = bin_rem[j] - weight  # запоминаем вес

        # ни одна корзина не может вместить предмет, создаем новую корзину
        if min_remainder == capacity + 1:
            bin_rem.append(capacity - weight)
            res += 1
        else:
            # кладем предмет в лучшую корзину
            bin_rem[best_bin] -= weight

    return res


if __name__ == '__main__':
    weights = [4, 4, 6, 6, 1, 8, 9, 1, 4, 2, 1]
    capacity = 10
    print(f"Минимальное количество необходимых корзин: {first_fit(weights, capacity)}")