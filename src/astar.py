from math import inf

from src.pqueue import PriorityQueue
from src.vstates import MatrixValuedStates, ValuedStates

# adjacency list
# incidence list
# adjacency matrix -> We can implement the costs in here...
# incidence matrix

# Adjacency matrix with cost values:
#   0 == No edge
#   N = cost
adjacency_mx = []


def get_path(meta: int, back_w: list):
    path = [meta]
    i = back_w[meta]
    while i is not None:
        path.append(i)
        i = back_w[i]

    return path[::-1]


def a_star(start: int, meta: int, vs: ValuedStates):
    f_costs = []
    g_costs = []
    back_w = []

    # TODO: For other problems we wont have the full size of the problem...
    #  We must implement getOrInf, getOrNone, insert(index)
    #  So we can use it to any given problem (like mosaics problem)
    for _ in range(vs.size()):
        f_costs.append(inf)
        g_costs.append(inf)
        back_w.append(None)

    pq = PriorityQueue()
    fs_cost = vs.get_h_cost(start, meta)

    pq.push((start, fs_cost))

    g_costs[start] = 0
    f_costs[start] = fs_cost

    while pq.size() > 0:
        crr, fn = pq.pop()
        if crr == meta:
            return get_path(crr, back_w), 0

        for des in vs.get_descendants(crr):
            gd = g_costs[crr] + vs.get_g_cost(crr, des)

            if gd < g_costs[des]:
                fd = gd + vs.get_h_cost(des, meta)

                g_costs[des] = gd
                f_costs[des] = fd
                back_w[des] = crr

                pq.push((des, fd))

    return None, 1


if __name__ == '__main__':
    vs = MatrixValuedStates(4)

    #   0 -(10)-> 1, 0 -(1)-> 2
    #   1 -(15)-> 2, 1 -(500)-> 3
    #   2 -(20)-> 3
    # Fastest path: 0 --> 1 --> 2 --> 3

    vs.add_edge(0, 1, 10)
    vs.add_edge(0, 2, 100)
    vs.add_edge(1, 2, 15)
    vs.add_edge(1, 3, 500)
    vs.add_edge(2, 3, 20)

    star, code = a_star(0, 3, vs)
    print(star)
