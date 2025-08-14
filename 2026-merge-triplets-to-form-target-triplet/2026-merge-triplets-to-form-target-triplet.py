class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # greddy approach
        a, b, c = target
        found0 = found1 = found2 = False
        
        for x, y, z in triplets:
            if x <= a and y <= b and z <= c:
                if x == a: found0 = True
                if y == b: found1 = True
                if z == c: found2 = True
        
        return found0 and found1 and found2
