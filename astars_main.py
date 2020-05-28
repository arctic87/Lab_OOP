import numpy as np
from astars_node import Node
from astars_function import Return
from astars_search import Search

if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0]]

    start = [0, 0]  # стартовая позиция
    end = [6, 6]  # конечная позиция
    cost = 1  # кол-во позиций проходимых за ход

    path = Search.search(None, maze, cost, start, end)
    #print(path)

    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row])for row in path]))