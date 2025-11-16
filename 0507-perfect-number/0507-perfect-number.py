class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        suma = 1  # zawsze dzielnik
        limit = int(sqrt(num))
        
        for i in range(2, limit + 1):
            if num % i == 0:
                suma += i
                if i * i != num:
                    suma += num // i
        
        return suma == num
