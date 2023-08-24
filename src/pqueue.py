from heapq import heappop, heappush


class PriorityQueue:
    def __init__(self):
        self._pq: list[tuple[float, int]] = []

    def pop(self) -> tuple[float, int]:
        return heappop(self._pq)

    def push(self, node: tuple[float, int]):
        heappush(self._pq, node)

    def size(self) -> int:
        return len(self._pq)

    def __repr__(self):
        return repr(self._pq)
