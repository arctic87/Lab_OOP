import numpy as np
from astars_node import Node

class Return:
    def return_path(self, current_node, maze):
        path = []
        no_rows, no_columns = np.shape(maze)
        # здесь мы инициализируем результирующий лабиринт с -1 в каждой позиции(текущей позиции)
        result = [[-1 for i in range(no_columns)] for j in range(no_rows)]
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        # возвращаем обратный путь
        path = path[::-1]
        start_value = 0
        # обновление пути (найденным A-star) от начала до конца. C каждым шагом, увеличиваем на 1
        for i in range(len(path)):
            result[path[i][0]][path[i][1]] = start_value
            start_value += 1
        return result


