from src.vstates import ValuedStates
import random


# Mosaics:
#   | 7 | 2 | 4 |       | 1 | 2 | 3 |
#   | 5 |   | 6 |  -->  | 4 | 5 | 6 |
#   | 8 | 3 | 1 |       | 7 | 8 |   |
# 0 Will be used to represent the "empty" block


def generate_random_mosaic():
    arr = []
    while len(arr) == 0 or not is_solvable(arr):
        arr = random.sample(range(0, 9), 9)

    return arr


def is_solvable(arr: list):
    c = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] != 0 and arr[j] != 0 and arr[i] > arr[j]:
                c += 1

    return c % 2 == 0


class MosaicValuedStates(ValuedStates):

    def __init__(self, initial_state=None):
        self._mosaic_list = []
        self._id_counter = 0

        self._new_mosaic(generate_random_mosaic() if initial_state is None else initial_state)

    def is_meta(self, s: int, e: int = None):
        _, mosaic = self._mosaic_list[s]
        for i in range(len(mosaic) - 1):
            if i + 1 != mosaic[i]:
                return False

        return True

    def _new_mosaic(self, new_mosaic: list[int]) -> tuple[bool, int]:
        """

        @param new_mosaic:
        @return: True if created new mosaic index and the mosaic's id
        """
        mid = self._id_counter
        has_m = False
        for saved_id, mosaic in self._mosaic_list:
            if mosaic == new_mosaic:
                mid = saved_id
                has_m = True
                return False, mid

        if not has_m:
            self._id_counter += 1

        mosaic = (mid, new_mosaic)
        self._mosaic_list.append(mosaic)
        return True, mid

    def get_g_cost(self, s: int, e: int) -> float:
        """
        g_cost will be the real cost... Will always be one
        """
        return 1

    def get_h_cost(self, s: int, e: int) -> float:
        """
        h_cost will be Manhattan distance
        """
        _, mosaic = self._mosaic_list[s]

        # First we will use number of deallocated pieces
        total_dst = 0
        for i in range(len(mosaic) - 1):
            total_dst += mosaic[i] != i + 1
        total_dst += mosaic[len(mosaic) - 1] != 0

        return total_dst

    def get_descendants(self, s: int) -> list[int]:
        d = []
        _, mosaic = self._mosaic_list[s]

        def flip(a, b):
            arr = mosaic[:]
            arr[a], arr[b] = arr[b], arr[a]

            new, m_id = self._new_mosaic(arr)

            if new:
                d.append(m_id)

        for i in range(9):
            if mosaic[i] == 0:
                if i == 0:
                    #   |   | 2 | 4 |
                    #   | 5 | 7 | 6 |
                    #   | 8 | 3 | 1 |
                    flip(i, i + 1)
                    flip(i, i + 3)
                elif i == 1:
                    #   | 2 |   | 4 |
                    #   | 5 | 7 | 6 |
                    #   | 8 | 3 | 1 |
                    flip(i, i + 1)
                    flip(i, i - 1)
                    flip(i, i + 3)
                elif i == 2:
                    #   | 2 | 4 |   |
                    #   | 5 | 7 | 6 |
                    #   | 8 | 3 | 1 |
                    flip(i, i + 3)
                    flip(i, i - 1)
                elif i == 3:
                    #   | 2 | 4 | 5 |
                    #   |   | 7 | 6 |
                    #   | 8 | 3 | 1 |
                    flip(i, i + 1)
                    flip(i, i + 3)
                    flip(i, i - 3)
                elif i == 4:
                    #   | 2 | 4 | 5 |
                    #   | 7 |   | 6 |
                    #   | 8 | 3 | 1 |
                    flip(i, i + 1)
                    flip(i, i - 1)
                    flip(i, i + 3)
                    flip(i, i - 3)
                elif i == 5:
                    #   | 2 | 4 | 5 |
                    #   | 7 | 6 |   |
                    #   | 8 | 3 | 1 |
                    flip(i, i - 1)
                    flip(i, i + 3)
                    flip(i, i - 3)
                elif i == 6:
                    #   | 2 | 4 | 5 |
                    #   | 7 | 6 | 8 |
                    #   |   | 3 | 1 |
                    flip(i, i + 1)
                    flip(i, i - 3)
                elif i == 7:
                    #   | 2 | 4 | 5 |
                    #   | 7 | 6 | 8 |
                    #   | 3 |   | 1 |
                    flip(i, i - 1)
                    flip(i, i + 1)
                    flip(i, i - 3)
                elif i == 8:
                    #   | 2 | 4 | 5 |
                    #   | 7 | 6 | 8 |
                    #   | 3 | 1 |   |
                    flip(i, i - 1)
                    flip(i, i - 3)

        return d

    def translate(self, arr: list[int]):
        r = []
        for i in arr:
            r.append(self._mosaic_list[i][1])
        return r

    def size(self):
        return 362_880  # Created while I don't implement a new star algorithm that does't need size
