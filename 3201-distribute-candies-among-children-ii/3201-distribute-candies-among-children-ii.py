class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # szybka kombinacja nCk (zwraca 0 jeśli k<0 lub k>n)
        def nCk(n: int, k: int) -> int:
            if k < 0 or k > n:
                return 0
            k = min(k, n - k)
            res = 1
            for i in range(1, k + 1):
                res = res * (n - k + i) // i
            return res

        # szybkie obliczenie C(s+2, 2) = (s+2)*(s+1)//2, ale zwracamy 0 jeśli s<0
        def C_s_plus_2_choose_2(s: int) -> int:
            if s < 0:
                return 0
            return (s + 2) * (s + 1) // 2

        # jeśli limit >= n to brak ograniczeń (stars-and-bars)
        if limit >= n:
            return C_s_plus_2_choose_2(n)

        total = 0
        comb3 = [1, 3, 3, 1]  # C(3, j) dla j = 0..3

        for j in range(0, 4):  # stała liczba iteracji
            s = n - j * (limit + 1)
            if s < 0:
                continue
            sign = -1 if (j % 2 == 1) else 1
            total += sign * comb3[j] * C_s_plus_2_choose_2(s)

        return total