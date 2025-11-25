class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # bo na koncu musi byc parzyste dla dzielenia przez 2
        # no i 0/5 dla piatki
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        
        # z dirichleta wynika, że jeśli reszta 0 istnieje,
        # to znajdziemy ją w maksymalnie k krokach.
        for length in range(1, k + 1):
            # Zamiast budować wielką liczbę, obliczamy tylko nową resztę
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length
                
        return -1