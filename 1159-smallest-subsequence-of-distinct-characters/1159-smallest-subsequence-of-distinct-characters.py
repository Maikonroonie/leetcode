class Solution:
    def smallestSubsequence(self, s: str) -> str:
        taken = set()
        freq = Counter(s) # robi słownik co ile razy wystepuje
        stack = []


        for st in s:

            freq[st] -= 1
            if st in taken:
                continue
            
            while stack and stack[-1] > st and freq[stack[-1]] > 0: # czyi jeszcze gdzies dalej w stringu
            # jest ten element ktory chcemy zpopowac to go popujemy
                x = stack.pop()
                taken.remove(x)
            
            stack.append(st)
            taken.add(st)

        res = ''
        for i in range(len(stack)):
            res += stack[i]

        return res


