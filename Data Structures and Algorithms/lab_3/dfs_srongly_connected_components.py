# Алгоритм поиска количества и состава сильно связных компонент:
# 1) Создается пустое множество для отслеживания посещенных вершин
# и пустой стек для записи вершин в порядке их завершения обхода
# 2) Для каждой вершины vertex в графе выполняются следующие шаги:
#       - Если вершина еще не была посещена:
#           * Помещение вершины vertex в множество посещенных вершин
#           * Для каждой смежной вершины adj_vertex исходящей из vertex, выполняются следующие действия:
#               - Если вершина еще не была посещена, рекурсивно вызывается функция обхода в глубину для adj_vertex
#           * После завершения обхода в глубину для всех смежных вершин vertex, эта вешина добавляется в стек
# 3) Создается транспонированный граф путем инвертирования всех ребер исходного графа
# 4) Пока стек не пуст, выполняются следующие действия (обход в глубину в транспонированном графе):
#       - Извлечение вершины:
#       - Если вершина vertex еще не была посещена:
#           * Создается новая компонента связности component
#           * Рекурсивно вызывается функция обхода в глубину для vertex в транспонированном графе,
#           принадлежащую компоненте component
#           * Компонента component содержит все вершины, достижимые из vertex в транспонированном графе
#           * Компонента component добавляется в список всех сильно связных компонент

def dfs(graph, vertex, visited, stack):
    visited[vertex] = True # посетили вершину
    for adj_vertex in graph[vertex]:
        if not visited[adj_vertex]:
            dfs(graph, adj_vertex, visited, stack)  # рекурсивно обходим все смежные вершины текущей вершины
    stack.append(vertex)


def get_transpose(graph): # транспонируем исходный графа
    num_vertices = len(graph)
    transpose = [[] for _ in range(num_vertices)]
    for vertex in range(num_vertices):
        for adj_vertex in graph[vertex]:
            transpose[adj_vertex].append(vertex)
    return transpose


def get_scc(graph): # ищем сильно связные компоненты в графе
    num_vertices = len(graph)
    visited = [False] * num_vertices
    stack = []

    # Обход графа в глубину и заполнение стека в порядке завершения обхода вершин
    for vertex in range(num_vertices):
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)

    # Получение транспонированного графа
    transpose = get_transpose(graph)
    visited = [False] * num_vertices
    scc_components = []

    # Обход транспонированного графа для каждой вершины в порядке, определенном стеком
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs(transpose, vertex, visited, component)
            scc_components.append(component)
    return scc_components


def read_graph_from_file(): # чтение файла
    graph_data = []
    with open('../graphs_examples/input.txt', 'r') as file:
        for line in file:
            row = line.strip().split()
            graph_data.append(row)

    vertices = graph_data[0][1:]
    graph = [[] for _ in range(len(vertices))]

    for i in range(1, len(graph_data)):
        edges = graph_data[i][1:]
        for j, edge in enumerate(edges):
            if edge == '1':
                graph[i - 1].append(j)

    return graph


def write_results_to_file(scc_components): # запись результатов в файл
    with open('../graphs_examples/output.txt', 'w') as file:
        file.write(f"Количество сильно связных компонент: {len(scc_components)}\n")
        file.write("Состав сильно связных компонент:\n")
        for scc in scc_components:
            vertices = [chr(vertex + 65) for vertex in scc]  # Преобразование индексов в вершины (A, B, C, ...)
            file.write(' '.join(vertices) + '\n')


# Чтение
graph = read_graph_from_file()

# Приск
scc_components = get_scc(graph)

# Запись
write_results_to_file(scc_components)