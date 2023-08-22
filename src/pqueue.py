from heapq import heappop, heappush


class PriorityQueue:
    def __init__(self):
        self._pq: list[tuple[int, float]] = []

    def pop(self) -> tuple[int, float]:
        return heappop(self._pq)

    def push(self, node: tuple[int, float]):
        heappush(self._pq, node)

    def size(self) -> int:
        return len(self._pq)

    def __repr__(self):
        return repr(self._pq)
