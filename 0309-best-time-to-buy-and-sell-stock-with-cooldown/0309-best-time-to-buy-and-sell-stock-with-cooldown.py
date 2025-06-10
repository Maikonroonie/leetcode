class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        n = len(prices)
        # DP tabela gdzie dp[i][0] - nie posiadam akcji w dniu i
        # dp[i][1] - posiadam akcje w dniu i
        dp = [[0] * 2 for _ in range(n + 2)]
        
        # Inicjalizacja - po ostatnim dniu nie możemy mieć zysku
        dp[n][0] = dp[n][1] = 0
        
        for i in range(n - 1, -1, -1):
            # Stan 0: Nie posiadam akcji (mogę kupić lub czekać)
            dp[i][0] = max(dp[i + 1][1] - prices[i],  # Kupuję
                          dp[i + 1][0])               # Czekam
            
            # Stan 1: Posiadam akcje (mogę sprzedać lub czekać)
            dp[i][1] = max(dp[i + 2][0] + prices[i],  # Sprzedaję (cooldown i+2)
                          dp[i + 1][1])               # Czekam
        
        return dp[0][0]  # Maksymalny zysk zaczynając od dnia 0 bez akcji

'''        
class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        dp = {} #key=(i, buying(true/false)) if 
        def dfs(i, buying):
            if i>= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell=dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)'''


