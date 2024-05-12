# Функция для проверки, является ли граф эйлеровым
def count(graph):
    # Подсчитываем количество вершин с нечетной степенью
    odd = 0
    for row in graph:
        degree = sum(row)
        if degree % 2 == 1:
            odd += 1
    # Граф эйлеров, если все вершины имеют четную степень
    return odd == 0

# Функция для проверки, является ли ребро мостом в графе
def is_bridge(graph, u, v):
    # Копируем граф
    graph_copy = [row[:] for row in graph]
    # Удаляем ребро из копии графа
    graph_copy[u][v] = 0
    graph_copy[v][u] = 0
    # Проверяем, связен ли граф после удаления ребра
    visited = [False] * len(graph)
    dfs(graph_copy, u, visited)
    return not visited[v]

# Функция для обхода графа в глубину
def dfs(graph, v, visited):
    # Помечаем вершину как посещенную
    visited[v] = True
    # Перебираем соседние вершины
    for u in range(len(graph)):
        if graph[v][u] == 1 and not visited[u]:
            # Удаляем ребро из графа
            graph[v][u] = 0
            graph[u][v] = 0
            # Рекурсивно обходим соседнюю вершину
            dfs(graph, u, visited)

# Функция для нахождения эйлерова цикла в графе
def find_eulerian_cycle(graph):
    # Проверяем, является ли граф эйлеровым
    if not count(graph):
        return None
    # Количество вершин в графе
    n = len(graph)
    # Стек для хранения текущего пути
    stack = []
    # Список для хранения эйлерова цикла
    cycle = []
    # Начинаем с произвольной вершины (например, с нулевой)
    stack.append(0)
    # Пока стек не пуст
    while stack:
        # Берем вершину из стека
        v = stack[-1]
        # Пока есть непосещенные ребра из этой вершины
        found = False
        for u in range(n):
            if graph[v][u] == 1:
                if not is_bridge(graph, v, u):
                    found = True
                    break
        if found:
            # Удаляем ребро из графа и добавляем новую вершину в стек
            graph[v][u] = 0
            graph[u][v] = 0
            stack.append(u)
        else:
            # Добавляем вершину в цикл
            cycle.append(stack.pop())
    # Возвращаем цикл в обратном порядке
    return cycle[::-1]

# Пример использования
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

cycle = find_eulerian_cycle(graph)
if cycle:
    print("Эйлеров цикл:", cycle)
else:
    print("Граф не является эйлеровым")