class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        for num, idx_list in d.items():
            idx_list.sort()
            n = len(idx_list)
            for i in range(n-1):
                if abs(idx_list[i] - idx_list[i+1]) <= k:
                    return True
        return False
            

        