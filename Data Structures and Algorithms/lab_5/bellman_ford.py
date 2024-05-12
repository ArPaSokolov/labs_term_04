# чтение графа из файла
def read_graph():
    # открываем файл для чтения
    with open('../graphs_examples/input.txt', "r") as f:
        line = f.readline()
        # количество строк и начальная вершина
        n, s = map(int, line.split())
        # создаем пустой список смежности
        adj = [[] for _ in range(n)]
        # Читаем матрицу смежности построчно
        for i in range(n):
            # преобразуем строку в список целых чисел
            row = list(map(int, f.readline().split()))
            # для каждого элемента строки
            for j in range(n):
                # если элемент не равен нулю
                if row[j] != 0:
                    # добавляем ребро (i, j) с весом row[j]
                    adj[i].append((j, row[j]))
    # возвращаем граф в виде списка смежности
    return adj, s

# алгоритм Беллмана-Форда
def bellman_ford(adj, s):
    # получаем количество вершин графа
    n = len(adj)
    # инициализируем массив расстояний до бесконечности
    dist = [float("inf")] * n
    # инициализируем массив предков пустыми значениями
    prev = [None] * n
    # устанавливаем расстояние от начальной вершины до себя равным нулю
    dist[s] = 0
    # повторяем n - 1 раз
    for _ in range(n - 1):
        # для каждого ребра (u, v) с весом w в графе
        for u in range(n):
            for v, w in adj[u]:
                # если расстояние до u + вес ребра меньше текущего расстояния до v
                if dist[u] + w < dist[v]:
                    # обновляем расстояние до v и предка v
                    dist[v] = dist[u] + w
                    prev[v] = u
    return dist, prev, s

# функция для вывода кратчайших путей из начальной вершины в файл
def print_paths(filename, s, dist, prev):
    # открываем файл для записи
    with open(filename, "w") as f:
        # для каждой вершины графа
        for v in range(len(dist)):
            # если вершина не является начальной
            if v != s:
                # если расстояние до нее конечно
                if dist[v] != float("inf"):
                    # выводим расстояние и путь до нее в файл без индексов (нумерация с единицы)
                    f.write(f"Путь от {s + 1} до {v + 1}: ")
                    path = []
                    cur = v
                    while cur is not None:
                        path.append(cur + 1)
                        cur = prev[cur]
                    path.reverse()
                    f.write(f"Расстояние: {dist[v]}\n")
                    f.write(" -> ".join(map(str, path)) + "\n")
                else:
                    # выводим сообщение о недостижимости вершины в файл без индексов (нумерация с единицы)
                    f.write(f"Вершина {v + 1} недостижима из {s + 1}\n")

# пример
graph = read_graph()
adj, s = graph[0], graph[1]
# Выполняем алгоритм Беллмана-Форда для графа и начальной вершины s
result = bellman_ford(adj, s)
# Если алгоритм успешно завершился
print_paths('../graphs_examples/output.txt', s, result[0], result[1])