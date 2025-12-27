class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        busy_rooms = [] # end, idx
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)
        
        usage_count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_idx)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                current_end, room = heapq.heappop(busy_rooms)
                new_end = current_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))
            
            usage_count[room] += 1
        
        return usage_count.index(max(usage_count))