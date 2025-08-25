class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        heap = []
        buy = prices[0]
        profit = 0
        prev = prices[0]


        for i in range(1, n):
            if prices[i] < prev:
                if heap:  # możemy sprzedać
                    sell = -heapq.heappop(heap)  # odwrócenie znaku
                    profit += sell - buy
                    heap.clear()
                buy = prices[i]

            elif prices[i] > prev:
                heapq.heappush(heap, -prices[i])
            prev = prices[i]
        
        if heap:  # sprzedaż na koniec, jeśli coś zostało
            profit += -heapq.heappop(heap) - buy

        return profit

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
'''
