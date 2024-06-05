import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.colors = {}  # R слева, В справа

    def add_edge(self, h_from, h_to):
        self.adjacency_list[h_from] = self.adjacency_list.get(h_from, []) + [h_to]
        self.adjacency_list[h_to] = self.adjacency_list.get(h_to, []) + [h_from]


    # обход в ширину для раскраски графа
    def bfs(self, vertex_start: int):
        remove_edges = []
        queue = [vertex_start]
        self.colors[vertex_start] = 'R'

        while queue:
            vertex_now = queue.pop(0)
            for vertex_to in self.adjacency_list[vertex_now]:
                if self.colors[vertex_to] and self.colors[vertex_now] == self.colors[vertex_to]:
                    remove_edges.append([vertex_now, vertex_to])
                elif not self.colors[vertex_to]:
                    self.colors[vertex_to] = 'R' if self.colors[vertex_now] == 'B' else 'B'
                    queue.append(vertex_to)
        return remove_edges

    # определяем является ли граф двудольным ^
    def check_dicotyledonous(self):
        self.colors = {vertex: "" for vertex in self.adjacency_list.keys()}

        remove_edges = []
        for vertex in self.adjacency_list.keys():
            if not self.colors[vertex]:
                remove_edges += self.bfs(vertex)
            return remove_edges


    # алгоритм Форда-Фалкерсона
    def algorithm_ford_fulkerson(self):
        # создаем новый граф, где
        adjacency_list_new = {'s': []}
        # вершины цвета R, становятся смежными с истоком, а вершины цвета B, становятся смежными со стоком
        for vertex_from, color in self.colors.items():
            if color == 'R':  # вершина смежна с истоком
                adjacency_list_new['s'].append(vertex_from)
                adjacency_list_new[vertex_from] = []
                for vertex_to in self.adjacency_list[vertex_from]:
                    adjacency_list_new[vertex_from].append(vertex_to)
            else:
                adjacency_list_new[vertex_from] = ['t']  # сток

        # запускаем цикл пока существует путь увеличения
        while True:
            path_vertex = ['s']
            # выполняется поиск пути увеличения с помощью рекурсивной функции dfs_algorithm_ford_fulkerson
            # если путь увеличения найден, происходит обновление графа
            if self.dfs_algorithm_ford_fulkerson(adjacency_list_new, path_vertex):
                path_vertex = path_vertex[1:-1]
                adjacency_list_new['s'].remove(path_vertex[0])  # удаляем ребра s -> u и v -> t
                adjacency_list_new[path_vertex[-1]].remove('t')
                for i in range(len(path_vertex) - 1):
                    adjacency_list_new[path_vertex[i]].remove(path_vertex[i + 1])
                    adjacency_list_new[path_vertex[i + 1]].append(path_vertex[i])  # добавляем ребра u -> v в v -> U
            else:
                break

        matching_max = []
        adjacency_list_new.pop('s')
        # просмотриваем оставшиеся ребра в графе
        for vertex_from, color in self.colors.items():
            if color == 'B':  # если вершина смежна со стоком
                for vertex_to in adjacency_list_new[vertex_from]:
                    if vertex_to != 't':  # если не равна стоку, добавляем в список
                        matching_max.append([vertex_from, vertex_to])

        # в результате получаем максимальное паросочетание
        return matching_max

    # рекурсивный поиск пути увеличения в графе ^
    def dfs_algorithm_ford_fulkerson(self, adjacency_list_new, path_vertex):
        # функция начинает с исходной вершины s и идет по смежным вершинам
        # если вершина t достигнута, функция возвращает True, указывая на наличие пути увеличения
        vertex_now = path_vertex[-1]
        if vertex_now == 't':
            return True

        # если это не так, функция продолжает искать путь, добавляя новые вершины к текущему пути
        for vertex_to in adjacency_list_new[vertex_now]:
            if vertex_to not in path_vertex:
                path_vertex.append(vertex_to)
                if self.dfs_algorithm_ford_fulkerson(adjacency_list_new, path_vertex):
                    #  вершина t достигнута
                    return True

        # если путь увеличения не найден, последний добавленный элемент удаляется из пути
        path_vertex.pop(-1)
        return False


    # поиск в глубину
    def dfs_algorithm_kuna(self, vertex, visited_vertices: list, matching_dict: dict):
        # если вершина уже была посещена
        if vertex in visited_vertices:
            return False  # путь увеличения не найден

        # добавляем в список посещенных вершин
        visited_vertices.append(vertex)
        # итерация по всем смежным вершинам
        for vertex_to in self.adjacency_list[vertex]:
            # проверяем вляется ли вершина непаросочетанной или можно ли найти путь увеличения из нее
            if matching_dict[vertex_to] == -1 or self.dfs_algorithm_kuna(matching_dict[vertex_to], visited_vertices, matching_dict):
                # текущая вершина становится паросочетанной с вершиной vertex_to
                matching_dict[vertex_to] = vertex
                return True

        #  все смежные вершины были просмотрены и не удалось найти путь увеличения
        return False

    # алгоритм Куна
    def algorithm_kuna(self):
        matching_dict = {}  # словарь для хранения текущего паросочетания

        # каждую вершину цвета 'B' обозначим непаросочетанной
        for vertex_from, color in self.colors.items():
            if color == 'B':
                matching_dict[vertex_from] = -1

        # поиском в глубину ищем пути увеличения из каждой вершины цвета 'R'
        for vertex_from, color in self.colors.items():
            visited_vertices = []
            if color == 'R':
                self.dfs_algorithm_kuna(vertex_from, visited_vertices, matching_dict)

        matching_max = []
        # просмотриваем все пары вершин в словаре
        for vertex_to, vertex_from in matching_dict.items():
            # если вершина не непаросочетанная
            if vertex_from != -1:
                matching_max.append([vertex_from, vertex_to])  # эта пара добавляется в список

        # возвращаеv максимальное паросочетание
        return matching_max


    # изображение графа
    def draw_graph(self, file_name, edges_red=None):
        edges_red_draw = []

        if edges_red is None:
            edges_red = []
        for vertex1, vertex2 in edges_red:
            edges_red_draw.append([vertex1, vertex2])
            edges_red_draw.append([vertex2, vertex1])

        left_side = []
        right_side = []
        for vertex, color in self.colors.items():
            if color == 'R':
                left_side.append(vertex)
            else:
                right_side.append(vertex)

        graph_draw = nx.DiGraph()
        for vertex_from in self.adjacency_list.keys():
            for vertex_to in self.adjacency_list[vertex_from]:
                graph_draw.add_edge(vertex_from, vertex_to)

        pos = {}
        x, y = 0., 0.
        for vertex in left_side:
            pos[vertex] = [x, y]
            y += 0.1
        x, y = 0.01, 0.

        for vertex in right_side:
            pos[vertex] = [x, y]
            y += 0.1

        if not pos:
            pos = nx.circular_layout(graph_draw)
        nx.draw(graph_draw, pos, with_labels=True)
        nx.draw_networkx_edges(graph_draw, pos, edgelist=edges_red_draw, edge_color="red")
        plt.savefig(file_name)
        plt.clf()


# демонстрация кода
graph = Graph()
edges_list = [(14, 13), (7, 8), (2, 7), (9, 15), (14, 9), (8, 9), (2, 9), (15, 3), (2, 4), (15, 10),
              (12, 13), (5, 3), (2, 10), (2, 11), (6, 12), (12, 7), (3, 12), (15, 11), (12, 16),
              (4, 15), (15, 7), (5, 7), (16, 2), (14, 11), (4, 14), (8, 11), (9, 12), (5, 13),
              (6, 5), (5, 11)]

for edge in edges_list:
    graph.add_edge(*edge)

graph_name = "graph.png"
graph.draw_graph(graph_name)
print(f"Исходный граф находится в файле {graph_name}")

remove_edges_list = graph.check_dicotyledonous()
if remove_edges_list:
    print("Граф не является двудольным. Нужно удалить некоторые ребра")
    # graph.remove_edges(remove_edges_list)
else:
    print("Граф является двудольным. Ничего удалять не надо.")

graph_name = "dicotyledonous_graph.png"
graph.draw_graph(graph_name)
print(f"Двудольный граф находится в файле {graph_name}")

matching_list_edges = graph.algorithm_ford_fulkerson()
graph_name = "ford_fulkerson_graph.png"
graph.draw_graph(graph_name, matching_list_edges)
print(f"Наибольшее паросочетание по алгоритму Форда-Фалкерсона: {len(matching_list_edges)}")
print(f"Двудольный граф с максимальным паросочетание по алгоритму Форда-Фалкерсона находится в файле {graph_name}")
matching_list_edges = graph.algorithm_kuna()
graph_name = "kun_graph.png"
graph.draw_graph(graph_name, matching_list_edges)
print(f"Наибольшее паросочетание по алгоритму Куна: {len(matching_list_edges)}")
print(f"Двудольный граф с максимальным паросочетание по алгоритму Куна находится в файле {graph_name}")
