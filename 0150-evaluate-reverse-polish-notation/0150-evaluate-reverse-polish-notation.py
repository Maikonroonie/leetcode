class Solution(object):
    def evalRPN(self, tokens): # rozwiazanie rekurencyjne
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

# rozwizanie za pomocą stacka
'''
        class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
'''

            
                