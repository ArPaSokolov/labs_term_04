import math # для бесконечности

file = open('../graphs_examples/input.txt', "r") # открываем файл для чтения
lines = file.readlines() # читаем все строки из файла
file.close() # закрываем файл

n, s = map(int, lines[0].split()) # считываем количество вершин в графе и стартовую вершину из первой строки
adj = [] # создаем пустой список для матрицы смежности
for i in range(1, n + 1): # перебираем строки от 1 до n
    row = list(lines[i].replace('inf', str(math.inf)).split())
    # преобразуем строку в список чисел, заменяя 'inf' на math.inf, преобразуем строку в список чисел
    adj.append(row) # добавляем список в матрицу смежности

dist = [math.inf] * n # создаем массив расстояний от s до каждой вершины и заполняем бесконечностями
visited = [False] * n # создаем массив флагов посещения каждой вершины и заполняем false

dist[s] = 0 # расстояние от s до себя равно 0
queue = [s] # добавляем s в очередь

while queue: # пока очередь не пуста
    u = min(queue, key=lambda x: dist[x]) # находим вершину с минимальным dist[u]
    queue.remove(u) # удаляем ее из очереди
    visited[u] = True # помечаем ее как посещенную
    for v in range(n): # перебираем все вершины графа
        if not visited[v]: # если v еще не посещена
            if dist[v] > dist[u] + float(adj[u][v].replace('inf', str(math.inf))): # если найден более короткий путь:
              dist[v] = dist[u] + float(adj[u][v].replace('inf', str(math.inf))) # обновляем расстояние до v
            if v not in queue: # если v еще не в очереди
              queue.append(v) # добавляем v в очередь

with open('../graphs_examples/output.txt', "w") as f:
    f.write(f'Кратчайшие расстояния от, {s}, до всех остальных вершин:\n')
    for i in range(n): # выводим результаты
      f.write(f'{i} {dist[i]}\n')