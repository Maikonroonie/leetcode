class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        
        # Jeśli suma jest nieparzysta, nie można jej podzielić na dwie równe części
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1): # tutaj musimy tak isc zeby dwa razy np nie doadac tego sameo numa,  gdybysmy szli na odwrot to ten element pod nami moglby sie zjebac np dp[4] = dp[2] or dp[4], gdzie gdzie dla num =2 dp od dwa dopiero co ustawilismy na true i tu by sie znow ustawilo wiec zle
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
