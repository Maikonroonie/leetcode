class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = len(apple)
        m = len(capacity)
        all = sum(apple)
        capacity.sort(reverse = True)
        res = 0
        p = 0
        while all > 0 and p<m:
            all -= capacity[p]
            res += 1
            p += 1
        return res