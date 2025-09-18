import heapq
from typing import List, Dict, Tuple

class TaskManager:
    """
    Operacje O(log n):
      - add / edit: push do kopca + update w mapie
      - rmv: usunięcie z mapy (leniwe kasowanie w kopcu)
      - execTop: czyszczenie nieaktualnych wpisów i pop
    Zasady wyboru: największy priority, a przy remisie większy taskId.
    """

    def __init__(self, tasks: List[List[int]]):
        # kopiec przechowuje krotki (-priority, -taskId)
        self._heap: List[Tuple[int, int]] = []
        # taskId -> (userId, priority) — źródło prawdy
        self._info: Dict[int, Tuple[int, int]] = {}

        for userId, taskId, priority in tasks:
            self._info[taskId] = (userId, priority)
            heapq.heappush(self._heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self._info[taskId] = (userId, priority)
        heapq.heappush(self._heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self._info[taskId]  # gwarantowane istnienie
        self._info[taskId] = (userId, newPriority)
        heapq.heappush(self._heap, (-newPriority, -taskId))  # leniwe

    def rmv(self, taskId: int) -> None:
        # usuwamy ze źródła prawdy; stare wpisy w kopcu zignorujemy
        self._info.pop(taskId, None)

    def _clean(self) -> None:
        # wywal nieaktualne/stare rekordy z wierzchołka kopca
        while self._heap:
            neg_p, neg_t = self._heap[0]
            taskId = -neg_t
            priority = -neg_p
            data = self._info.get(taskId)
            if data is None:
                heapq.heappop(self._heap)     # zadanie usunięte
                continue
            _, cur_p = data
            if cur_p != priority:
                heapq.heappop(self._heap)     # wpis nieaktualny (po edycji)
                continue
            break  # top jest spójny ze stanem w _info

    def execTop(self) -> int:
        self._clean()
        if not self._heap:
            return -1
        _, neg_t = heapq.heappop(self._heap)
        taskId = -neg_t
        userId, _ = self._info.pop(taskId)
        return userId
