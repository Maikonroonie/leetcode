class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # we need gcm and lcm
        def gcd(a, b): #NWD
            while b:
                a, b = b, a % b
            return a
         
        def lcm(a, b): # NWW
            return (a*b)//(gcd(a, b))

        stack = []
        for num in nums:
            stack.append(num)
            
            while len(stack)>1:
                g = gcd(stack[-1], stack[-2])
                if g == 1:
                    break
                b = stack.pop()
                stack[-1] = lcm(stack[-1], b)

        return stack
