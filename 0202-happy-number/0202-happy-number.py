class Solution:
    def isHappy(self, n: int) -> bool:
        def transform(val):
            res = 0
            for char in str(val):
                res += int(char)**2
            return res

        seen = set()
        
        while n != 1:
            if n in seen:
                return False # Cycle detected
            
            seen.add(n)
            n = transform(n)
            
        return True
