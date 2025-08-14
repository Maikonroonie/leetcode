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
