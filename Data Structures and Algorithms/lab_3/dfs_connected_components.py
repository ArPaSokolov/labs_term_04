# Алгоритм с использованием обхода в глубину:
# 1) Создается пустое множество для отслеживания посещенных вершин и пустой список для хранения компонент связности
# 2) Для каждой вершины в графе выполняются следующие шаги:
#       - Если вершина еще не была посещена:
#           * Вершина становится начальной точкой для новой компоненты связности
#           * Создается пустой список для хранения вершин текущей компоненты связности
#           * Запускается рекурсивная функция обхода в глубину, начиная с текущей вершины.
#           Во время обхода в глубину для каждой смежной вершины, которая еще не была посещена,
#           выполняются следующие действия:
#               - Помещение вершины в множество посещенных вершин
#               - Добавление вершины в список текущей компоненты связности
#               - Рекурсивный вызов функции обхода в глубину для смежной вершины.
#       - Если вершина уже была посещена, то это означает, что она уже принадлежит какой-то компоненте связности,
#       и ее обход в рамках текущей итерации алгоритма не требуется
# 3) По завершении обхода в глубину, список текущей компоненты связности содержит все вершины,
# принадлежащие этой компоненте связности
# 4) Список текущей компоненты связности добавляется в список всех компонент связности
class Graph:
    def __init__(self): # графа в виде словаря
        self.graph = {}

    def add_vertex(self, vertex): # добавление новой вершины в граф
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v): # создание связи между двумя вершинами
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited, component): # обход в глубину для поиска компоненты связности
        visited.add(vertex)
        component.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited: # смотрим, посетили ли соседние вершин
                self.dfs(neighbor, visited, component)

    def find_connected_components(self): # поиск компонент связности в графе
        visited = set()
        components = []
        for vertex in self.graph: # поиск компоненты связности, начиная с текущей вершины
            if vertex not in visited:
                component = []
                self.dfs(vertex, visited, component)
                components.append(component)
        return len(components), components


def read_graph_from_file(): # чтение из файла
    graph = Graph()
    with open('../graphs_examples/input.txt', 'r') as file:
        lines = file.readlines()
        vertices = lines[0].strip().split()[1:]
        for line in lines[1:]:
            data = line.strip().split()
            vertex = data[0]
            edges = data[1:]
            for i in range(len(edges)):
                if edges[i] == '1':
                    graph.add_edge(vertex, vertices[i])

        # учитываем вершины, которые не имеют ребер с другими вершинами
        isolated_vertices = set(vertices) - set(graph.graph.keys())
        for vertex in isolated_vertices:
            graph.add_vertex(vertex)

    return graph


def write_results_to_file(num_components, components): # запись результатов в файл
    with open('../graphs_examples/output.txt', 'w') as file:
        file.write(f'Количество компонент связности: {num_components}\n')
        file.write('Состав компонент связности:')
        for component in components:
            file.write("{" + ' '.join(component) + '} ')


# Чтение
graph = read_graph_from_file()

# Поиск
num_components, components = read_graph_from_file().find_connected_components()

# Запись
write_results_to_file(num_components, components)
