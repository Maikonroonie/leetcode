class Solution(object):
    def longestPalindrome(self, s):
        '''# first idea, here we go from the middle to the left and rigth tracking the longest palindrom
        # we do it twice first if the len of palindrom is the even number and second time when it is 
        # and odd number, we return the res that is the longer one
        n=len(s)
        res=""
        res_len=0
        for i in range(n):
            l ,r = i, i
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>res_len:
                    res=s[l:r+1]
                    res_len=r-l+1
                l-=1
                r+=1
        for i in range(n):
            l ,r = i, i+1
            while l>=0 and r<n and s[l]==s[r]:
                if (r-l+1)>res_len:
                    res=s[l:r+1]
                    res_len=r-l+1
                l-=1
                r+=1
        return res'''

        #second idea is dynamic programinng approach:
        # dp[i][j] = True means that substring from index i to j is a palindrom
        def dynamic(s):
            n=len(s)
            if n == 0:
                return ""
            elif n==1:
                return s
            elif n==2 and s[0]==s[1]:
                return s
            elif n==2:
                return s[0]
            dp=[[False for _ in range(n)] for _ in range(n)]
            start=0
            max_len=1
            for i in range(n):
                dp[i][i] = True
            
            for i in range(n-1):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    start=i
                    max_len=2
            for i in range(3, n+1):
                for j in range(n-i+1):
                    k=j+i-1
                    if s[j] == s[k] and dp[j+1][k-1]:
                        dp[j][k] = True
                        if i > max_len:
                            start = j
                            max_len = i

            return s[start:start + max_len]
        return dynamic(s)
