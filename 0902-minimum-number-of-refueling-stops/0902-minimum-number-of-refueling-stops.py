#Jedziemy w stronę target, zaczynając z startFuel.

#Po drodze mijamy stacje – wrzucamy ich paliwo do max-heapa (kolejki priorytetowej, największe paliwo na #górze).

#Jeśli w danym momencie paliwa nam brakuje, to tankujemy z najlepszej dotychczas miniętej stacji (czyli #bierzemy największe paliwo z heapa).

#Powtarzamy, aż dotrzemy do celu lub nie ma już możliwości tankowania.

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # max-heap (w Pythonie heapq jest min-heap, więc wrzucamy wartości ujemne)
        max_heap = []
        fuel = startFuel
        prev = 0
        ans = 0
        stations.append([target, 0])  # traktujemy cel jak "stację" z paliwem 0

        for pos, cap in stations:
            fuel -= pos - prev  # zużywamy paliwo dojazdem do tej stacji
            while fuel < 0 and max_heap:  # nie starczyło paliwa, tankujemy
                fuel += -heapq.heappop(max_heap)
                ans += 1
            if fuel < 0:  # nie możemy dotrzeć
                return -1
            heapq.heappush(max_heap, -cap)  # zapisujemy paliwo z tej stacji
            prev = pos
        
        return ans
 
    
    
    '''
    
            #first i ll try dp aproach O(n^2)
    class Solution:
        def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
            # dp[k] - maksymalny zasięg po k tankowaniach

            n = len(stations)
            dp = [0 for _ in range(n+1)]
            dp[0] = startFuel

            for i, (pos, fuel) in enumerate(stations):
                # iterujemy wstecz, aby nie nadpisać wyników w tym samym kroku
                for k in range(i, -1, -1):
                    if dp[k] >= pos:  # jeśli możemy dotrzeć do stacji
                        dp[k+1] = max(dp[k+1], dp[k] + fuel)
            
            # szukamy minimalnej liczby tankowań, która pozwala dotrzeć do celu
            for k, dist in enumerate(dp):
                if dist >= target:
                    return k

            return -1

    '''
