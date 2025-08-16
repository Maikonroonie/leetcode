class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n=len(intervals) # number of intervals
        if n==0: return 0
        
        intervals.sort(key=lambda x: x[1]) # sortujemy po czasie zakonczenia
        res=[]

        # we add two points to the res the optimal greedy way to do it is to append
        # end point and one less from that point
        res.append(intervals[0][1] -1)
        res.append(intervals[0][1])

        for i in range(1, n):
            start = intervals[i][0]
            end = intervals[i][1]

            last = res[-1] # the largest point
            second_last = res[-2] # the second largest

            if start > last: # none of the points can currently cover up this interval
                res.append(end -1)
                res.append(end)
            elif start == last: 
                res.append(end)
            elif start > second_last:
                res.append(end)
        return len(res)


        