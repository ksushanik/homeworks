"""
Графы. Создание матрицы смежности

Граф задан числом вершин N и ребрами их связывающими. Каждое ребро задано парой чисел (номерами вершин,
которые оно связывает). Рёбра вводятся либо с клавиатуры, либо задаются в виде массива размера 2*K,
где K - число рёбер.
Необходимо построить матрицу смежности в виде квадратного массива.
"""


def build_adjacency_matrix(N, edges):
    # Создаем пустую матрицу смежности размером N x N, заполненную нулями
    adjacency_matrix = [[0] * N for _ in range(N)]

    # Заполняем матрицу смежности на основе введенных ребер
    for edge in edges:
        vertex1, vertex2 = edge
        adjacency_matrix[vertex1][vertex2] = 1
        adjacency_matrix[vertex2][vertex1] = 1

    return adjacency_matrix


# Пример использования функции:
N = 5  # Количество вершин
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (2, 0), (2, 4)]  # Пример списка ребер

adj_matrix = build_adjacency_matrix(N, edges)

# Вывод матрицы смежности
for row in adj_matrix:
    print(row)

