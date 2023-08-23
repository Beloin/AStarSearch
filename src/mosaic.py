from src.vstates import ValuedStates
import random

# Mosaics:
#   | 7 | 2 | 4 |       | 1 | 2 | 3 |
#   | 5 |   | 6 |  -->  | 4 | 5 | 6 |
#   | 8 | 3 | 1 |       | 7 | 8 |   |


# 0 Will be used to represent the "empty" block

mosaic_example = []


class MosaicValuedStates(ValuedStates):

    def __init__(self):
        self._mosaic_list = []
        self._id_counter = 0

        self.mosaic = self.new_mosaic(random.sample(range(0, 9), 8))

    def new_mosaic(self, new_mosaic):
        mosaic = (self._id_counter, new_mosaic)
        self._mosaic_list.append(mosaic)
        self._id_counter += 1
        return mosaic

    def get_g_cost(self, s: int, e: int) -> float:
        """
        g_cost will be the real cost... Will always be one
        """
        pass

    def get_h_cost(self, s: int, e: int) -> float:
        """
        h_cost will be Manhattan distance
        """
        _, mosaic = self._mosaic_list[s]

        # First we will use number of deallocated pieces
        total_dst = 0
        for i in range(9):
            total_dst += mosaic[i] != i

        return total_dst

    def get_descendants(self, s: int) -> list[int]:
        d = []
        _, mosaic = self._mosaic_list[s]

        def flip(a, b):
            arr = mosaic[:]
            arr[a], arr[b] = arr[b], arr[a]

            d.append(self._id_counter)
            self.new_mosaic(arr)

        for i in range(9):
            if mosaic[i] == 0:
                if i == 0:
                    flip(i, i+1)
                    flip(i, i+3)
                    new_mosaic_01 = mosaic[:]
                    new_mosaic_01[0], new_mosaic_01[1] = new_mosaic_01[1], new_mosaic_01[0]

                    d.append(self._id_counter)
                    self.new_mosaic(new_mosaic_01)

                    new_mosaic_02 = mosaic[:]
                    new_mosaic_02[0], new_mosaic_02[3] = new_mosaic_02[3], new_mosaic_02[0]

                    d.append(self._id_counter)
                    self.new_mosaic(new_mosaic_02)
                elif i == 1:
                    new_mosaic_01 = mosaic[:]
                    new_mosaic_01[1], new_mosaic_01[0] = new_mosaic_01[0], new_mosaic_01[1]

                    d.append(self._id_counter)
                    self.new_mosaic(new_mosaic_01)

                    new_mosaic_02 = mosaic[:]
                    new_mosaic_02[1], new_mosaic_02[4] = new_mosaic_02[4], new_mosaic_02[1]

                    d.append(self._id_counter)
                    self.new_mosaic(new_mosaic_02)

                    new_mosaic_03 = mosaic[:]
                    new_mosaic_02[1], new_mosaic_02[4] = new_mosaic_02[4], new_mosaic_02[1]

    def size(self):
        return 100_000  # Created while I don't implement a new star algorithm that does't need size
