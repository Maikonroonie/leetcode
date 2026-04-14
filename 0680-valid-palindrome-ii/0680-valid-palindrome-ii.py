class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        n = len(s)
        l, r = 0, n-1
        flag = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skip_left = is_palindrome(l+1, r)
                skip_right = is_palindrome(l, r-1)
                return skip_left or skip_right
        return True

        