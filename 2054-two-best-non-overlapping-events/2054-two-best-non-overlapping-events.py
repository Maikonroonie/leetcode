class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        start_sorted = sorted(events)
        end_sorted = sorted(events, key=lambda x: x[1])
        end_sorted = deque(end_sorted)

        res = max(v for s, e, v in events)
        end_max = 0

        for s, e, v in start_sorted:
            while end_sorted and end_sorted[0][1] < s:
                _, _, val = end_sorted.popleft()
                end_max = max(end_max, val)
            res = max(res, v + end_max)
        
        return res
            


        