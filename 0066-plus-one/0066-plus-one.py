class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        t = n - 1
        
        while t >= 0:
            if digits[t] < 9:
                digits[t] += 1
                return digits
            digits[t] = 0
            t -= 1
            
        return [1] + digits