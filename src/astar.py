from math import inf
from typing import Union

from src.pqueue import PriorityQueue
from src.vstates import MatrixValuedStates, ValuedStates


def a_star(vs: ValuedStates, start: int, meta: Union[None, int] = None):
    f_costs = {}
    g_costs = {}
    back_w = {}

    pq = PriorityQueue()
    fs_cost = vs.get_h_cost(start, meta)

    pq.push((fs_cost, start))

    g_costs[start] = 0
    f_costs[start] = fs_cost

    while pq.size() > 0:
        fn, crr = pq.pop()

        if vs.is_meta(crr, meta):
            return get_path(crr, back_w), 0

        descendants = vs.get_descendants(crr)
        for des in descendants:
            gd = g_costs[crr] + vs.get_g_cost(crr, des)

            if gd < get_value_or_inf(g_costs, des):
                fd = gd + vs.get_h_cost(des, meta)

                g_costs[des] = gd
                f_costs[des] = fd
                back_w[des] = crr

                pq.push((fd, des))

    return None, 1


def get_path(meta: int, back_w: dict):
    path = [meta]
    i = back_w[meta]
    while i is not None:
        path.append(i)
        i = back_w.get(i)

    return path[::-1]


def get_value_or_inf(arr: list | dict, i: int):
    item = arr.get(i)
    return inf if item is None else item


if __name__ == '__main__':
    vs = MatrixValuedStates(4)

    #   0 -(10)-> 1, 0 -(100)-> 2
    #   1 -(15)-> 2, 1 -(500)-> 3
    #   2 -(20)-> 3
    # Fastest path: 0 --> 1 --> 2 --> 3

    vs.add_edge(0, 1, 10)
    vs.add_edge(0, 2, 100)
    vs.add_edge(1, 2, 15)
    vs.add_edge(1, 3, 500)
    vs.add_edge(2, 3, 20)

    star, code = a_star(vs, 0, 3)
    print(star)
