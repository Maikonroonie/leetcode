class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(wage)
        # k is the amount of guys we want to hire
        A=[]
        for i in range(n):
            A.append((wage[i]/quality[i], quality[i])) # placa / wydajnosc - najoptymalniejsi pracownicy
        A.sort()
        
        # every worker at the end will get same money ratio (wage[i]/wage[j] = quality[i]/quality[j])
        # so at first we add first k workers with the bes efiicinecy ( ratio ), and then we follow the min
        # res while adding next workers we increase ratio but we reduce money, becouse we keep in heap max
        # qualities what going further we remove from the (potential hiring staff) at the end we have
        # the minimum value which is sum(quality) * (ratio(wage / quality) - currently the biggest)

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


        