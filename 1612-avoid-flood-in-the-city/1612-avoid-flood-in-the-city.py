class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [1] * n               # domyślnie 1 w dniach suchych, -1 w dniach deszczu
        last_full = {}              # last_full[lake] = index ostatniego dnia, kiedy jezioro #było zalane
        dry_heap = []               # min-heap indeksów suchych dni (te indeksy < aktualny index)

        for i, lake in enumerate(rains):
            if lake == 0:
                # dzień suchy — dodajemy jego indeks do heapu, wynik tymczasowo ustawiony na 1
                heapq.heappush(dry_heap, i)
                res[i] = 1
            else:
                # dzień deszczu — wynik musi być -1
                res[i] = -1
                if lake in last_full:
                    t = last_full[lake]   # musimy znaleźć suchy dzień j: t < j < i
                    temp = []
                    # wyrzucamy suche dni które są <= t (nie nadają się dla tego jeziora)
                    while dry_heap and dry_heap[0] <= t:
                        temp.append(heapq.heappop(dry_heap))
                    # teraz pierwsze w heap (jeśli istnieje) jest > t
                    if not dry_heap:
                        # brak dostępnego suchego dnia do wysuszenia tego jeziora przed dzisiejszym deszczem
                        return []
                    # używamy najmniejszego możliwego suchego dnia > t
                    dry_index = heapq.heappop(dry_heap)
                    res[dry_index] = lake
                    # odtworzyć wyrzucone elementy z powrotem do heapu
                    for x in temp:
                        heapq.heappush(dry_heap, x)
                # oznaczamy, że jezioro jest teraz pełne (ostatni dzień zalania = i)
                last_full[lake] = i

        # wszystkie pozostałe dni suszenia pozostają 1 (takie wymaganie zadania)
        return res
