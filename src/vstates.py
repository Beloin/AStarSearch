import abc
import math


def h(s, e):
    return ((math.pow(math.e, -s / 2)) * 10) * e


class ValuedStates(abc.ABC):

    @abc.abstractmethod
    def get_g_cost(self, s: int, e: int) -> float:
        pass

    @abc.abstractmethod
    def get_h_cost(self, s: int, e: int) -> float:
        pass

    @abc.abstractmethod
    def get_descendants(self, s: int) -> list[int]:
        pass

    @abc.abstractmethod
    def size(self) -> int:
        pass


class MatrixValuedStates(ValuedStates):

    def __init__(self, vertices: int):
        self._size = vertices
        self.mx: list[list[float]] = []
        for i in range(vertices):
            self.mx.append([0 for _ in range(vertices)])

    def add_edge(self, v1: int, v2: int, cost: float):
        self.mx[v1][v2] = cost

    def get_g_cost(self, s: int, e: int) -> float:
        return self.mx[s][e]

    def get_h_cost(self, s: int, e: int) -> float:
        return h(s, e)

    def get_descendants(self, s: int) -> list[int]:
        desc = []
        for index, cost in enumerate(self.mx[s]):
            if cost > 0:
                desc.append(index)
        return desc

    def size(self) -> int:
        return self._size

    def __repr__(self):
        return repr(self.mx)
