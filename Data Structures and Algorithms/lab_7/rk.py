# Функция для вычисления хеша подстроки длины m
def hash(s, m):
  h = 0
  p = 31 # Простое число
  q = 10**9 + 9 # Большое простое число
  for i in range(m):
    h = (h * p + ord(s[i])) % q # Вычисляем хеш по формуле
  return h

# Функция для поиска всех подстрок t в строке s с помощью алгоритма Рабина-Карпа
def rabin_karp_all(s, t):
  n = len(s) # Длина строки
  m = len(t) # Длина подстроки
  if m > n: # Если подстрока длиннее строки, то нет совпадений
    return []
  p = 31 # Простое число
  q = 10**9 + 9 # Большое простое число
  t_hash = hash(t, m) # Хеш подстроки
  s_hash = hash(s[:m], m) # Хеш первой подстроки строки длины m
  pm = pow(p, m-1, q) # Степень p по модулю q
  result = [] # Список для хранения индексов начала подстрок в строке
  for i in range(n-m+1): # Перебираем все возможные позиции подстроки в строке
    if t_hash == s_hash: # Если хеши совпадают, то проверяем на равенство подстроки
      if s[i:i+m] == t: # Если подстроки равны, то добавляем индекс начала подстроки в список
        result.append(i)
    if i < n-m: # Если не дошли до конца строки, то обновляем хеш следующей подстроки строки длины m
      s_hash = (s_hash - ord(s[i]) * pm) * p + ord(s[i+m]) % q # Вычитаем старший символ и добавляем младший по формуле

  return result # Возвращаем список индексов начала подстрок в строке

# Пример использования функции rabin_karp_all
with open('input.txt', 'r') as f:
  s = f.readline()
t = "^_^" # Подстрока
indexes = rabin_karp_all(s, t) # Список индексов начала подстрок в строке или пустой список, если нет совпадений
print(indexes) # Выводим результат на экран

# O(mn), m - длина подстроки, n - длина строки
