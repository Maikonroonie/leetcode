class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        '''
        d = defaultdict(int)
        for digit in digits:
            if digit not in d:
                d[digit] = 1
            else:
                d[digit] += 1
        for digit, times in d.items():
        res = 0
        '''
        d = set()
        res = 0
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        num = 100*digits[i] + 10*digits[j] + digits[k]
                        if num not in d and num % 2 == 0 and num >= 100:
                            res += 1
                            d.add(num)
        return res





