class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        
        # Dodajemy wartowniki (balony o wartości 1) na początku i końcu
        # Ułatwia to obliczenia dla skrajnych przypadków
        new_nums = [1] + nums + [1]
        
        # Inicjalizacja tablicy DP:
        # dp[l][r] - maksymalna liczba monet jaką można zdobyć z przedziału balonów od l do r (włącznie)
        # Rozmiar (n+2) x (n+2) ponieważ dodaliśmy dwa wartowniki
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Wypełniamy tablicę DP od najkrótszych przedziałów do najdłuższych
        # l - lewy koniec przedziału
        for l in range(n, 0, -1):  # Iterujemy od końca do początku (od n do 1)
            # r - prawy koniec przedziału (musi być >= l)
            for r in range(l, n + 1):
                # i - indeks ostatniego balonu do usunięcia w przedziale [l, r]
                # Sprawdzamy wszystkie możliwości wyboru ostatniego balonu
                for i in range(l, r + 1):
                    # Obliczamy liczbę monet z usunięcia balonu i:
                    # new_nums[l-1] * new_nums[i] * new_nums[r+1] to monety za aktualny balon
                    # dp[l][i-1] to maksymalna liczba monet z lewej części
                    # dp[i+1][r] to maksymalna liczba monet z prawej części
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    
                    # Aktualizujemy maksymalną wartość dla przedziału [l, r]
                    dp[l][r] = max(dp[l][r], coins)
        
        # Wynik to maksymalna liczba monet dla całego przedziału [1, n]
        # (pomijamy wartowników)
        return dp[1][n]