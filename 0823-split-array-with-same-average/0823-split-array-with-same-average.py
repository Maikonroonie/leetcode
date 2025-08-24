from collections import defaultdict

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # optymalizacja: jeśli n == 1, nie da się podzielić
        if n == 1:
            return False

        # dp[k] = zbiór sum możliwych dla podzbioru długości k
        dp = [set() for _ in range(n+1)]
        dp[0].add(0)

        for num in nums:
            # aktualizujemy od tyłu, żeby nie nadpisać bieżącej iteracji
            for k in range(n-1, 0, -1):
                for s in dp[k-1]:
                    dp[k].add(s + num)

        # sprawdzamy dla każdego możliwego k
        for k in range(1, n):
            if (total * k) % n == 0:  # musi być całkowita suma
                target = (total * k) // n
                if target in dp[k]:
                    return True

        return False

'''            
    # O(n*2^n)
    # brute force ktory wypierdala time limit
    class Solution:
        def splitArraySameAverage(self, nums: List[int]) -> bool:
            n=len(nums)
            total = sum(nums)

            for mask in range(1, (1<<n) -1):
                sumA = 0
                lenA = 0

                for i in range(n):
                    if (mask>>i) & 1:
                        sumA += nums[i]
                        lenA +=1
                if float(sumA/lenA) == float(total/n):
                    return True
            return False
'''