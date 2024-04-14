# Алгоритм поиска кратчайшего пути:
# 1) Инициализируем очередь и добавляем в нее начальную вершину
# 2) Инициализируем список расстояний distances, где для каждой вершины расстояние устанавливается -1,
# а для начальной вершины 0
# 3) Пока очередь не пуста, выполняем следующие действия:
#   * Извлекаем вершину из начала очереди
#   * Для каждой смежной вершины, которая еще не была посещена, делаем следующее:
#       - Если расстояние до смежной вершины больше, чем расстояние до текущей вершины плюс 1, то обновляем расстояние
#       - Добавляем смежную вершину в очередь для дальнейшего исследования.

def bfs_shortest_paths(graph, start_vertex):
    vertices = list(graph.keys())  # список вершин графа
    num_vertices = len(vertices)  # общее количество вершин в графе
    distances = [-1] * num_vertices  # кратчайшие расстояния от начальной вершины до каждой вершины в графе
    distances[vertices.index(start_vertex)] = 0 # кратчайшие расстояния от начальной вершины до себя
    queue = [start_vertex]  # инициализация очереди и добавление начальной вершины
    front = 0  # индекс следующего элемента в очереди
    while front < len(queue):
        current_vertex = queue[front]  # извлечение вершины из начала очереди
        front += 1
        for neighbor_index, has_edge in enumerate(graph[current_vertex]):
            if has_edge and (distances[neighbor_index] == -1 or distances[neighbor_index] > distances[vertices.index(current_vertex)] + 1):
                # Если расстояние до смежной вершины больше, чем расстояние до текущей вершины плюс 1,
                # обновляем расстояние
                distances[neighbor_index] = distances[vertices.index(current_vertex)] + 1
                queue.append(vertices[neighbor_index])  # добавляем смежную вершину в очередь
    return distances


def read_graph_from_file(): # чтение из файла
    graph = {}
    with open('../graphs_examples/input.txt', 'r') as file:
        lines = file.readlines()
        vertices = lines[0].split()[1:]
        adjacency_matrix = [[int(x) for x in line.strip().split()[1:]] for line in lines[1:]]
        for i, vertex in enumerate(vertices):
            graph[vertex] = adjacency_matrix[i]
    return graph


def write_results_to_file(vertices, distances): # запись результатов в файл
    with open('../graphs_examples/output.txt', 'w') as file:
        for vertex, distance in enumerate(distances):
            if distance == -1:
                distance = "inf"
            file.write(f"{vertices[vertex]} {distance}\n")


# Чтение
graph = read_graph_from_file()

# Поиск
start_vertex = 'A' # начальная вершина
distances = bfs_shortest_paths(graph, start_vertex)

# Запись
write_results_to_file(list(graph.keys()), distances)
