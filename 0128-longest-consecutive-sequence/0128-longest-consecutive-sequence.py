class Solution(object):
    def longestConsecutive(self, nums):
        #uzywamy seta i sprawdzamy gdzie sie zaczyna sekwencja (num-1) i liczymy dlugosc kazdej w nums
        numset = set(nums)
        max_len = 0
        for num in numset:
            if num - 1 not in numset:
                length = 1
                x = num + 1
                while x in numset:
                    length += 1
                    x += 1
                max_len = max(max_len, length)
        return max_len