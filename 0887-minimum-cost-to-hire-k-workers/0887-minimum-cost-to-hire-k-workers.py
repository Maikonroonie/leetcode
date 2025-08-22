class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(wage)
        # k is the amount of guys we want to hire
        A=[]
        for i in range(n):
            A.append((wage[i]/quality[i], quality[i])) # placa / wydajnosc - najoptymalniejsi pracownicy
        A.sort()
        
        heap=[]
        money = 0
        res = inf
        for efficiency, quality in A:
            heapq.heappush(heap, -quality) #max heap
            money+= quality
            if len(heap) > k:
                money +=heapq.heappop(heap) #we have -valus in heap
            if len(heap) == k:
                res=min(res, money * efficiency)
        
        return res


        