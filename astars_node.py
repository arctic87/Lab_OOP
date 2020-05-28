class Node:
    """
        Класс узла
        Node(Узел) - все потенциальные позиции или остановки с уникальным идентификатором
        parent является родителем текущего узла
        position - текущая позиция Узла в лабиринте
        g - счетчик от начала лабиринта до текущего узла
        h - эвристический счетчик оставшихся ячеек от текущего узла до конечного узла
        f - общий счетчик текущего узла, то есть: f = g + h
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position