def read_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix


def convert_to_edges(matrix):
    V = len(matrix)  # количество вершин графа
    E = []  # список ребер графа (длина, вершина 1, вершина 2)
    for i in range(V):
        for j in range(i + 1, V):  # пропускаем диагональ и нижнюю половину матрицы
            if matrix[i][j] > 0:  # если есть ребро между вершинами i и j
                E.append((matrix[i][j], i + 1, j + 1))  # добавляем ребро в список
    return E


def convert_to_matrix(E):
    V = max(max(e[1], e[2]) for e in E)  # количество вершин графа
    M = [[0 for i in range(V)] for j in range(V)]  # матрица смежности графа

    for e in E:
        # для каждого ребра в списке
        i = e[1] - 1  # начало ребра
        j = e[2] - 1  # конец ребра
        w = e[0]  # длина ребра
        M[i][j] = w  # заполняем матрицу смежности
    return M


def kraskal(R):
    Rs = sorted(R, key=lambda x: x[0])
    U = set()  # список соединенных вершин
    D = {}  # словарь списка изолированных групп вершин
    T = []  # список ребер остова

    for r in Rs:
        if r[1] not in U or r[2] not in U:  # проверка для исключения циклов в остове
            if r[1] not in U and r[2] not in U:  # если обе вершины не соединены, то
                D[r[1]] = [r[1], r[2]]  # формируем в словаре ключ с номерами вершин
                D[r[2]] = D[r[1]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not D.get(r[1]):  # если в словаре нет первой вершины, то
                    D[r[2]].append(r[1])  # добавляем в список первую вершину
                    D[r[1]] = D[r[2]]  # и добавляем ключ с номером первой вершины
                else:
                    D[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
                    D[r[2]] = D[r[1]]

            T.append(r)  # добавляем ребро в остов
            U.add(r[1])  # добавляем вершины в множество U
            U.add(r[2])

    for r in Rs:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[2] not in D[r[1]]:  # если вершины принадлежат разным группам, то объединяем
            T.append(r)  # добавляем ребро в остов
            gr1 = D[r[1]]
            D[r[1]] += D[r[2]]  # объединем списки двух групп вершин
            D[r[2]] += gr1
    return T


if __name__ == '__main__':
    input_file = 'input.txt'
    # E = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]
    adjacency_matrix = read_adjacency_matrix(input_file)
    R = convert_to_edges(adjacency_matrix)
    with open('output.txt', 'w') as f:
        f.write('Минимальное остовное дерево: ' + str(kraskal(R)))