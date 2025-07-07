class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        result = [0 for _ in range(n)]
        stack = []  # indeksy

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        
        return result
