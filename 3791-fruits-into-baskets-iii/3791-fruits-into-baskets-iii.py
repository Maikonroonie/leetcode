'''
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        res = 0
        used = [False for _ in range(n)]
        for fruit in fruits:
            placed = False
            # szukamy lewego (first) wolnego kosza z capacity >= fruit
            for j in range(n):
                if not used[j] and baskets[j] >= fruit:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                res += 1

        return res
'''
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(baskets), int(sqrt(len(baskets)))
        block = [max(baskets[i:i+m]) for i in range(0, n, m)]
        res = 0
        for fruit in fruits:
            for b in range(len(block)):
                if block[b] >= fruit:
                    for i in range(b*m, min((b+1)*m, n)):
                        if baskets[i] >= fruit:
                            baskets[i] = 0
                            break
                    block[b] = max(baskets[b*m:(b+1)*m])
                    break
            else:
                res += 1
        return res 

# da sie to jeszcz zrobic przez segment tree

