from typing import Union
from math import inf

from src.pqueue import PriorityQueue
from src.vstates import ValuedStates


class IterativeAStar:
    def __init__(self, vs: ValuedStates, start: int, meta: Union[None, int] = None):
        self.meta = meta
        self.vs = vs

        self.f_costs = {}
        self.g_costs = {}
        self.back_w = {}

        self.pq = PriorityQueue()
        fs_cost = vs.get_h_cost(start, meta)

        self.pq.push((fs_cost, start))

        self.g_costs[start] = 0
        self.f_costs[start] = fs_cost

        self._crr = None
        self._crr_des = None

        self._finished = False
        self._result = None

    @staticmethod
    def get_path(meta: int, back_w: dict):
        path = [meta]
        i = back_w[meta]
        while i is not None:
            path.append(i)
            i = back_w.get(i)

        return path[::-1]

    @staticmethod
    def get_value_or_inf(arr: list | dict, i: int):
        item = arr.get(i)
        return inf if item is None else item

    def get_current(self):
        return self._crr

    def get_current_des(self):
        return self._crr_des

    def has_finished(self):
        return self._finished

    def ongoing(self):
        return not self.has_finished()

    def get_result(self):
        if self.has_finished():
            return self._result
        else:
            return None, 2

    def tick(self):
        if self.pq.size() == 0 or self._finished:
            if not self._finished:
                self._finished = True
                self._result = None, 1

            return

        fn, crr = self.pq.pop()
        self._crr = crr

        if self.vs.is_meta(crr, self.meta):
            self._result = self.get_path(crr, self.back_w), 0
            self._finished = True
            return

        descendants = self.vs.get_descendants(crr)
        self._crr_des = descendants

        for des in descendants:
            gd = self.g_costs[crr] + self.vs.get_g_cost(crr, des)

            if gd < self.get_value_or_inf(self.g_costs, des):
                fd = gd + self.vs.get_h_cost(des, self.meta)

                self.g_costs[des] = gd
                self.f_costs[des] = fd
                self.back_w[des] = crr

                self.pq.push((fd, des))
