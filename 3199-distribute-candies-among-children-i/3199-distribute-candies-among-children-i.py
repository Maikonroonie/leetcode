class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # n cukierkwo i 3 dzieci na ile sposobow mozna rozdzelic n cukierkow na 
        # 3 dzieci zeby zadne nie dostalo powyzej limint candies
        def silnia(n):
            wynik = 1
            for i in range(1, n + 1):
                wynik *= i
            return wynik


        def comb(n, k):
            return int(silnia(n)/(silnia(k) * silnia(n-k)))

        total = 0
        # inclusion-exclusion po tym ile zmiennych przekracza limit (0..3)
        for j in range(0, 4):
            s = n - j * (limit + 1)
            if s < 0:
                continue
            total += ((-1) ** j) * comb(3, j) * comb(s + 2, 2)

        return total

