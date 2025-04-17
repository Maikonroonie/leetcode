class Solution(object):
    def scheduleCourse(self, courses):
        #priority queue
        courses.sort(key=lambda x: x[1])
        heap=[]
        max_time = 0
        for time, end_time in courses:
            heapq.heappush(heap, -time)
            max_time+=time
            if max_time>end_time:
                max_time+=heapq.heappop(heap)
        return len(heap)