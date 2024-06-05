# Глобальные переменные
prime_number = 13
large_prime = 256


# вычисление хеша подстроки длины m
def calculate_hash(substring, length):
    hash_value = 0
    for i in range(length):
        hash_value = (hash_value * prime_number + ord(substring[i])) % large_prime
    return hash_value


# поиск всех подстрок pattern в строке text с помощью алгоритма Рабина-Карпа
def rabin_karp_all(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    # текст короче образа
    if pattern_length > text_length:
        return []

    pattern_hash = calculate_hash(pattern, pattern_length)
    text_hash = calculate_hash(text[:pattern_length], pattern_length)
    prime_power = prime_number ** (pattern_length - 1) % large_prime

    indexes = []
    # идем по всем подстрокам длины образа
    for i in range(text_length - pattern_length + 1):
        # проверка на совпадение хэша и подстроки
        if pattern_hash == text_hash and text[i:i+pattern_length] == pattern:
            indexes.append(i)
        # обновление хэша для следующей подстроки
        if i < text_length - pattern_length:
            text_hash = ((text_hash - ord(text[i]) * prime_power) * prime_number + ord(text[i+pattern_length])) % large_prime

    return indexes


# пример
text = "Practicing your comprehension of written English will both improve your vocabulary and understanding of grammar and word order."
pattern = "your"
indexes = rabin_karp_all(text, pattern)
print(indexes)
