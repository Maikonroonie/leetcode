class Solution(object):
    def isMatch(self, s, p):
        # Inicjalizacja tablicy DP:
        # dp[i][j] - czy podciąg s[i:] pasuje do wzorca p[j:]
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        
        # Warunek brzegowy: pusty string i pusty wzorzec pasują do siebie
        dp[len(s)][len(p)] = True

        # Wypełniamy tablicę DP od końca (od ostatnich znaków)
        for i in range(len(s), -1, -1):          # Iterujemy od końca stringa s
            for j in range(len(p) - 1, -1, -1):  # Iterujemy od końca wzorca p (bez ostatniego znaku)
                
                # Sprawdzamy czy aktualne znaki pasują:
                # - czy nie wyszliśmy poza zakres s
                # - czy znaki są identyczne lub wzorzec ma '.' (dowolny znak)
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                # Obsługa gwiazdki '*' (operator 0 lub więcej powtórzeń)
                if (j + 1) < len(p) and p[j + 1] == "*":
                    # Możliwość 1: traktujemy 'a*' jako 0 powtórzeń (pomijamy wzorzec)
                    dp[i][j] = dp[i][j + 2]
                    
                    # Możliwość 2: jeśli znaki pasują, traktujemy 'a*' jako 1+ powtórzeń
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                
                # Gdy nie ma gwiazdki, ale znaki pasują - przechodzimy do następnych znaków
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        # Wynik to czy cały string s pasuje do całego wzorca p
        return dp[0][0]
        