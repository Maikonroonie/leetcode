class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op != 'C' and op != 'D' and op != '+':
                res += int(op)
                stack.append(int(op))
            elif op == '+':
                x = stack.pop()
                y = stack.pop()
                res += x+y
                stack.append(y)
                stack.append(x)
                stack.append(x+y)
            elif op == 'C':
                x = stack.pop()
                res -= x
            elif op == 'D':
                x = stack.pop()
                res += 2*x
                stack.append(x)
                stack.append(2*x)
        return res

        