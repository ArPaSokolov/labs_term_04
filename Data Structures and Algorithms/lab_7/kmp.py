# нахождение префикс-функции строки
def prefix_function(pattern):
    # длина строки
    m = len(pattern)
    # значения префикс-функции
    pi = [0] * m
    # индекс для сравнения символов
    j = 0
    # идем по всем символам строки, начиная со второго
    for i in range(1, m):
        # пока j > 0 и символы не совпадают, уменьшаем j на значение префикс-функции предыдущего символа
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        # если символы совпадают, увеличиваем j на 1
        if pattern[i] == pattern[j]:
            j += 1
        # присваиваем значение j в список префикс-функции
        pi[i] = j
    # возвращаем список префикс-функции
    return pi

# поиск всех вхождений образца по алгоритму Кнута-Морриса-Пратта
def kmp_search(pattern, text):
    # длина образца
    m = len(pattern)
    # длина текста
    n = len(text)
    # вычисление префикс-функции образца
    pi = prefix_function(pattern)
    # индекс для сравнения символов образца и текста
    j = 0
    # список для хранения индексов вхождений
    matches = []
    # цикл по всем символам текста
    for i in range(n):
        # пока j > 0 и символы не совпадают, уменьшаем j на значение префикс-функции предыдущего символа образца
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        # если символы совпадают, увеличиваем j на 1
        if text[i] == pattern[j]:
            j += 1
        # если достигнут конец образца, добавляем индекс вхождения в список и
        # уменьшаем j на значение префикс-функции последнего символа образца
        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]
    # возвращаем список индексов вхождений
    return matches


with open("input.txt", "r") as file:
    text = file.read()

# ввод образца с клавиатуры
pattern = input("Введите образец: ")

# проверка, не пустой ли образец
if pattern:
    # поиск
    matches = kmp_search(pattern, text)
    # вывод результата на экран
    if matches:
        print("Образец найден в тексте на следующих позициях:")
        print(*matches)
    else:
        print("Образец не найден в тексте.")
else:
    print("Образец не может быть пустым.")