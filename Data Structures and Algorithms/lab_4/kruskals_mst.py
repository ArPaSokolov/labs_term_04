def convert_to_edges(matrix):
    num_vertices = len(matrix)  # количество вершин графа
    edges = []  # список ребер графа (длина, вершина 1, вершина 2)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # пропускаем диагональ и нижнюю половину матрицы
            if matrix[i][j] > 0:  # если есть ребро между вершинами i и j
                edges.append((matrix[i][j], i + 1, j + 1))  # добавляем ребро в список
    return edges


def convert_to_matrix(edges):
    num_vertices = max(max(e[1], e[2]) for e in edges)  # количество вершин графа
    adjacency_matrix = [[0 for i in range(num_vertices)] for j in range(num_vertices)]  # матрица смежности графа

    for edge in edges:
        # для каждого ребра в списке
        vertex1 = edge[1] - 1  # начало ребра
        vertex2 = edge[2] - 1  # конец ребра
        weight = edge[0]  # длина ребра
        adjacency_matrix[vertex1][vertex2] = weight  # заполняем матрицу смежности
    return adjacency_matrix


def kruskal(edges):
    sorted_edges = sorted(edges, key=lambda x: x[0])
    connected_vertices = set()  # список соединенных вершин
    disjoint_sets = {}  # словарь списка изолированных групп вершин
    minimum_spanning_tree = []  # список ребер остова

    for edge in sorted_edges:
        if edge[1] not in connected_vertices or edge[2] not in connected_vertices:
            if edge[1] not in connected_vertices and edge[2] not in connected_vertices:
                disjoint_sets[edge[1]] = [edge[1], edge[2]]  # формируем в словаре ключ с номерами вершин
                disjoint_sets[edge[2]] = disjoint_sets[edge[1]]  # и связываем их с одним и тем же списком вершин
            else:
                if not disjoint_sets.get(edge[1]):
                    disjoint_sets[edge[2]].append(edge[1])
                    disjoint_sets[edge[1]] = disjoint_sets[edge[2]]
                else:
                    disjoint_sets[edge[1]].append(edge[2])
                    disjoint_sets[edge[2]] = disjoint_sets[edge[1]]

            minimum_spanning_tree.append(edge)  # добавляем ребро в остов
            connected_vertices.add(edge[1])  # добавляем вершины в множество connected_vertices
            connected_vertices.add(edge[2])

    for edge in sorted_edges:
        if edge[2] not in disjoint_sets[edge[1]]:  # если вершины принадлежат разным группам, то объединяем
            minimum_spanning_tree.append(edge)  # добавляем ребро в остов
            group1 = disjoint_sets[edge[1]]
            disjoint_sets[edge[1]] += disjoint_sets[edge[2]]  # объединяем списки двух групп вершин
            disjoint_sets[edge[2]] += group1
    return minimum_spanning_tree


def read_graph_from_file():
    with open('../graphs_examples/input.txt', 'r') as file:
        lines = file.readlines()
        adjacency_matrix = [[int(x) for x in line.strip().split()[1:]] for line in lines[1:]]
    return adjacency_matrix


def write_tree_to_file(tree):
    with open('../graphs_examples/output.txt', 'w') as file:
        file.write('Минимальное остовное дерево: ' + str(tree))


adjacency_matrix = read_graph_from_file()
edges = convert_to_edges(adjacency_matrix)
minimum_spanning_tree = kruskal(edges)

write_tree_to_file(minimum_spanning_tree)
