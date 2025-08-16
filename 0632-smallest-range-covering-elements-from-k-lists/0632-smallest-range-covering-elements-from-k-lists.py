class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # the ,key is to track the minimum element from each list and sliding window to track the
        # range of numbers
        
        # Iterate through the lists by always popping the minimum element from the heap (by heap's nature) 
        # and checking the range between the minimum and the current maximum.
        n=len(nums) # the amount of lists
        heap = []
        cur_max = -float('inf')
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], i, 0)) # min heap we keep smallest elements on the top
            cur_max = max(cur_max, nums[i][0])
        small = [-float('inf'), float('inf')] # the range of current smalles slindng window
        while heap:
            cur_min, list_idx, i = heapq.heappop(heap)
            
            if cur_max - cur_min < small[1] - small[0]:
                small = [cur_min, cur_max] # updateing the range

            if i+1 < len(nums[list_idx]):
                nxt = nums[list_idx][i+1]
                heapq.heappush(heap, (nxt, list_idx, i+1))
                cur_max = max(cur_max, nxt)
            else:
                break
        return small

# in heap we always have one element of each list



