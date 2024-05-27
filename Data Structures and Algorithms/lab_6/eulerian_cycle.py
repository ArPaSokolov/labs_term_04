# проверка на эйлеров граф
def is_eulerian_cycle(matrix):
    n = len(matrix)  # количество вершин
    for i in range(n):
        degree = sum(matrix[i][j] != 0 for j in range(n))  # количество исходящих ребер
        if degree % 2 != 0:  # сли степень нечетная
            return False  # не имеет цикла Эйлера

    visited = [False] * n  # массив посещенных вершин
    dfs(matrix, 0, visited)  # проверка связности графа
    if all(visited):  # все вершины были посещены
        return True
    else:
        return False  # граф не связный


def dfs(matrix, vertex, visited):
    visited[vertex] = True
    for i in range(len(matrix)):
        if matrix[vertex][i] != 0 and not visited[i]:
            dfs(matrix, i, visited)


def find_eulerian_cycle(matrix):
    if not is_eulerian_cycle(matrix):  # существует ли цикл Эйлера
        return None

    n = len(matrix)  # количество вершин

    cycle = []  # список для хранения вершин цикла
    stack = [0]  # стек для обхода графа

    while stack:  # пока стек не пуст
        u = stack[-1]  # берем вершину с вершины стека
        flag = False  # было найдено не пройденное ребро
        for v in range(n):  # ищем не пройденное ребро из текущей вершины
            if matrix[u][v] > 0:
                stack.append(v)
                # удаляем ребро из графа
                matrix[u][v] -= 1
                matrix[v][u] -= 1
                flag = True
                break
        if not flag:  # если вершины нет среди не пройденных ребер, то добавляем ее в цикл и удаляем из стека
            cycle.append(stack.pop())

    cycle.pop()  # удаляем из стека вершину, в которую вернулись

    return cycle  # возвращаем цикл Эйлера


def read_graph():
    with open("../graphs_examples/input.txt", 'r') as file:
        lines = file.readlines()
        matrix = [[int(num) for num in line.split()] for line in lines]
    return matrix


def write_eulerian_cycle(cycle):
    with open("output.txt", 'w') as file:
        if eulerian_cycle:
            cycle_str = '->'.join(map(str, cycle))
            file.write("Эйлеров цикл: " + cycle_str)
        else:
            file.write("В графе нет эйлерова цикла")

matrix = read_graph()
eulerian_cycle = find_eulerian_cycle(matrix)
write_eulerian_cycle(eulerian_cycle)

# не эйлеров
# 0 1 1 1 0 0
# 1 0 1 1 1 0
# 1 1 0 1 0 1
# 1 1 1 0 1 1
# 0 1 0 1 0 1
# 0 0 1 1 1 0

# эйлеров
# 0 1 1 1 1 0
# 1 0 1 1 0 1
# 1 1 0 1 1 0
# 1 1 1 0 1 0
# 1 0 1 1 0 1
# 0 1 0 0 1 0
