# not vety optimal O(kn)
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        # zawsze bierzemy ten ktoru w danym momencie da najwiekszy zyst
        # pod warunkiem ze mamy wystarczająco kapitalu
        # w = capital that we have
        A=[]
        for i in range(n):
            A.append((profits[i], capital[i]))
        A.sort(reverse = True)
        cnt=0
        p=0
        seen = [False for _ in range(len(A))]
        while cnt!=k and p<len(A):
            val, cost = A[p]
            if cost>w or seen[p]:
                p+=1
            elif not seen[p]:
                seen[p] = True
                w+=val
                p=0
                cnt+=1
        print(A)
        return w
    '''
# second approach with heap 
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n=len(profits)
        A=[]
        for i in range(n):
            A.append((capital[i], profits[i]))
        A.sort()
        heap=[]
        i=0

        for _ in range(k):
            while i < len(A) and A[i][0] <=w:
                heapq.heappush(heap, -A[i][1]) # minus becouse we want max heap
                i+=1
            if not heap:
                break
            w+=-heapq.heappop(heap)
        return w









