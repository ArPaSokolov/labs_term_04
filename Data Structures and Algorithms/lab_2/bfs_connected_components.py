# Алгоритм нахождения количества и состава компонент связности:
# 1) Инициализация пустого списка для хранения компонент связности components
# 2) Инициализация пустого набора для отслеживания посещенных вершин visited_vertices
# 3) Для каждой вершины в графе:
#   - Если вершина не была посещена:
#          * Создаем новую компоненту связности.
#          * Выполняем поиск в ширину, начиная с этой вершины:
#               - Инициализируем очередь и добавляем в нее нашу вершину
#               - Пока queue не пуста:
#                   * Извлекаем текущую вершину из очереди.
#                   * Если текущая не была посещена:
#                      - Помечаем текущую вершину как посещенную и добавляем ее в visited_vertices
#                      - Добавляем текущую вершину в текущую компоненту связности
#                      - Для каждой смежной вершины neighbor с current_vertex:
#                          * Если neighbor не была посещена, добавляем ее в queue
#   - Если вершина была посещена:
#       * Добавляем текущую компоненту связности component в список components
# 4) Возвращаем количество компонент связности и список components с составом каждой компоненты

# Поиск всех компонент связности в графе
def find_connected_components(graph):
    visited = set() # вершины, которые уже обработаны
    components = [] # список компонент связности

    for vertex in graph:
        if vertex not in visited:
            component = bfs(graph, vertex, visited)
            components.append(component)

    return len(components), components # найденные компоненты и их длина


# Обход в ширину каждой компоненты
def bfs(graph, start_vertex, visited):
    queue = [start_vertex] # вершины, которые должны быть обработаны
    visited.add(start_vertex)
    component = []  # компонента связности

    while queue:
        current_vertex = queue.pop(0)
        component.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return component # список, содержащий вершины текущей компоненты связности


def read_graph_from_file(): # чтение из файла
    with open('../graphs_examples/input.txt', 'r') as file: # чтение из файла
        graph = {}  # граф в виде словаря
        lines = file.readlines()
        vertices = lines[0].split()[1:]  # список вершин из первой строки
        for i in range(1, len(lines)):
            row = lines[i].split()
            vertex = row[0]
            neighbors = [vertices[j] for j in range(len(row[1:])) if int(row[1:][j]) == 1]
            graph[vertex] = neighbors
    return graph


def write_results_to_file(num_components, components): # запись результатов в файл
    with open('../graphs_examples/output.txt', 'w') as file: # запись в файл
        file.write(f'Количество компонент связности: {num_components}\n')
        file.write('Состав компонент связности:')
        for component in components:
            file.write("{" + ' '.join(component) + '} ')


# Чтение
graph = read_graph_from_file()

# Поиск
num_components, components = find_connected_components(graph)

# Запись
write_results_to_file(num_components, components)
