class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # we want to construct a triangle with the biggest porimeter
        # so when we have a, b, c triangle can be formed if a + b > c and c > a and c > b

        nums.sort(reverse = True)

        a = None
        b = None
        c = None
        
        for num in nums:
            if c == None:
                c = num
            elif b == None:
                b = num
            elif a == None:
                a = num
            elif a + b > c:
                return a + b + c
            else:
                c = b
                b = a
                a = num
        if a != None and b != None and c != None:
            if a + b > c:
                return a + b + c
        return 0



        