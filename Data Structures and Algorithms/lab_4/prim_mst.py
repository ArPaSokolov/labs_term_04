# Функция для чтения матрицы смежности из файла
def read_adjacency_matrix():
    with open('../graphs_examples/input.txt', 'r') as f:
        lines = f.readlines()
        matrix = []
    for line in lines:
        row = [int(x) for x in line.split()]
        matrix.append(row)
    return matrix


# Функция для нахождения вершины с минимальным ключом среди непосещенных
def min_key(keys, visited):
    min = float("inf") # Бесконечность
    min_index = -1 # Индекс минимальной вершины
    for v in range(len(keys)): # Для каждой вершины
        if keys[v] < min and not visited[v]: # Если ключ меньше минимума и вершина не посещена
            min = keys[v] # Обновляем минимум
            min_index = v # Обновляем индекс
    return min_index # Возвращаем индекс


# Функция для реализации алгоритма Прима
def prim(graph):
    n = len(graph) # Количество вершин
    parent = [None] * n # Массив для хранения родителей в остовном дереве
    keys = [float("inf")] * n # Массив для хранения ключей (весов ребер)
    visited = [False] * n # Массив для отметки посещенных вершин
    keys[0] = 0 # Ключ первой вершины равен нулю
    parent[0] = -1 # Первая вершина не имеет родителя
    for i in range(n - 1): # Для каждой вершины кроме последней
        u = min_key(keys, visited) # Находим вершину с минимальным ключом среди непосещенных
        visited[u] = True # Помечаем ее как посещенную
        for v in range(n): # Для каждой смежной вершины
            if graph[u][v] > 0 and not visited[v] and graph[u][v] < keys[v]:
                # Если есть ребро и вершина не посещена и вес ребра меньше ключа
                parent[v] = u # Обновляем родителя
                keys[v] = graph[u][v] # Обновляем ключ
    return parent # Возвращаем массив родителей


# Преобразования массива родителей в список кортежей из трех элементов: номера вершины, номера родителя и веса ребра
def convert(parent, graph):
    result = [] # Список для хранения кортежей
    for v in range(1, len(parent)): # Для каждой вершины кроме первой
        u = parent[v] # Номер родителя
        w = graph[u][v] # Вес ребра
        result.append((v + 1, u + 1, w)) # Добавляем кортеж в список (прибавляем единицу к номерам вершин для удобства)
    return result # Возвращаем список


def write_results_to_file(result):
    with open('../graphs_examples/output.txt', 'w') as f:
        f.write("Минимальное остовное дерево: " + str(result))


# Пример
graph = read_adjacency_matrix() # Читаем матрицу смежности из файла
parent = prim(graph) # Находим минимальное остовное дерево
result = convert(parent, graph)
write_results_to_file(result)
