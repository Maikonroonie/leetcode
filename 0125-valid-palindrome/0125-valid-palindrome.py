class Solution(object):
    def isPalindrome(self, s):
        def is_in_alph(c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))


        n=len(s)
        left = 0
        right = n-1
        while left < right:
            while left<right and not is_in_alph(s[left]):
                left+=1
            while left<right and not is_in_alph(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
            