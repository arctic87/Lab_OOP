import numpy as np
from astars_node import Node
from astars_function import Return


class Search:
    def search(self, maze, cost, start, end):

     # Создаем начальный и конечный узел с инициализацией их значений g, h и f
        start_node = Node(None, tuple(start))
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0

    # Список не посещенных точек
        yet_to_visit_list = []
        # Список уже посещенных точек
        visited_list = []

        # Создаем начальный узел
        yet_to_visit_list.append(start_node)

        # Добавляем условия остановки. Кол-во допустимых шагов.
        # Для предотвращения бесконечного цикла, ставим адекватное кол-во итераций
        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 10

        # 4 варианта движения из каждой позиции (лево-право-низ-верх)
        # + добавим движение по диагонали вниз-вправо[1,1]
        move = [[-1, 0],  # идем вверх
                [0, -1],  # идем влево
                [1, 0],  # идем вниз
                [1, 1],  # идем вниз-вправо
                [0, 1]]  # идем вправо

        # лабиринт, кол-во строк и столбцов
        no_rows, no_columns = np.shape(maze)

        # Цикл, пока не найдем конец
        while len(yet_to_visit_list) > 0:

            # Каждый раз, когда попадаем на еще не посещенный узел, счетчик посещений повышается
            outer_iterations += 1

            # Текущий узел
            current_node = yet_to_visit_list[0]
            current_index = 0
            for index, item in enumerate(yet_to_visit_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # если мы попадаем в эту точку, значит вычислительная стоимость слишком высока
            if outer_iterations > max_iterations:
                print("невозможно расчитать путь, слишком много итераций")
                return Return.return_path(None, current_node, maze)

            #помещаем текущий узел в список посещенных
            yet_to_visit_list.pop(current_index)
            visited_list.append(current_node)

            # проверим достигли мы концечного узла или нет, если да, то построим путь
            if current_node == end_node:
                return Return.return_path(None, current_node, maze)

            # Генерация со всех соседних площадок
            children = []

            for new_position in move:

                # Определим позицию узла
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Убедимся, что в пределах досягаемости (проверим, в пределах лабиринта или нет)
                if (node_position[0] > (no_rows - 1) or
                        node_position[0] < 0 or
                        node_position[1] > (no_columns - 1) or
                        node_position[1] < 0):
                    continue

                # Проверка проходимости узла
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Cоздаем новый узел
                new_node = Node(current_node, node_position)

                # добавим новый узел
                children.append(new_node)

            # Дочерние узлы
            for child in children:

                # Поиск по всему списку посещений
                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                # создаем f, g, и h значения
                child.g = current_node.g + cost
                #здесь расчитываются эвристические затраты с использованием эвклидового расстояния
                child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                           ((child.position[1] - end_node.position[1]) ** 2))

                child.f = child.g + child.h

                # дочерний узел уже в списке не посещенных и значения g уже понижено
                if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                    continue

                # добавление в список еще не посещенных
                yet_to_visit_list.append(child)
            # дочерние узлы
            for child in children:

                # поиск по всему списку посещений
                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                # создаем f, g, и h значения
                child.g = current_node.g + cost
                #здесь расчитываются эвристические затраты с использованием эвклидового расстояния
                child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                           ((child.position[1] - end_node.position[1]) ** 2))

                child.f = child.g + child.h

                # дочерний узел уже в списке не посещенных и значения g понижено
                if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                    continue

                # добавление в список еще не посещенных
                yet_to_visit_list.append(child)
