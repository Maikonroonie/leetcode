class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import defaultdict
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]]+=1
        from heapq import nlargest
        return [key for key, value in nlargest(k, d.items(), key=lambda item: item[1])]
        

