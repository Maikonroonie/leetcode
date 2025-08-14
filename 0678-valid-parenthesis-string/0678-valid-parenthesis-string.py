#stack approach O(n), O(n)
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []  # indeksy '('
        star = []   # indeksy '*'
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                star.append(i)
            else:  # ch == ')'
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        # Dopasowanie pozostałych '(' z gwiazdkami
        while stack and star:
            if stack[-1] > star[-1]:  # gwiazdka musi być po '('
                return False
            stack.pop()
            star.pop()
        
        return not stack
'''
#best greddy approach O(n), O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0