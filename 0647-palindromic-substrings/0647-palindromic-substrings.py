class Solution(object):
    def countSubstrings(self, s):
        n=len(s) # dp[i][j]= true oznacza ze od idx i do j jest palindrom 
        if n==0:
            return 0
        cnt=0
        dp=[[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            cnt+=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                cnt+=1
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cnt+=1
        return cnt

