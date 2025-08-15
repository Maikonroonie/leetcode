'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or (n & (n - 1)) != 0:  # nie potęga 2 → false
            return False
        # przesuwamy bity parami
        while n > 1:
            n >>= 2
        return n == 1

# n & (n-1) == 0  - oznacza ze to jest potega dwojki bo taka liczba ma tylko jeden bit na 1 reszte na zero
# Potęgi 4 mają ustawiony bit co 2 pozycje, więc każde przesunięcie o 2 pozycje w prawo usuwa dokładnie dwa zera.
#W końcu zostanie 1, jeśli to potęga 4.