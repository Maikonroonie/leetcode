class Solution(object):
    def evalRPN(self, tokens):
        def operation(a, b, op):
            if op == '+':
                return a+b
            if op == '-':
                return a-b
            if op == '*':
                return a*b
            if op == '/':
                return int(a / b) if a * b >= 0 else -(-a // b)
        res=0
        def rek():
            token = tokens.pop()
            if token not in '+-*/':
                return int(token)
            
            right = rek()
            left = rek()
            
            return int(operation(left, right, token))
            
        return rek()

            
                