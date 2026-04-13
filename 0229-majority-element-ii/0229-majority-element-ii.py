class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # wiecej niz 1/3 razy
        # no to wiadomo ze mozna by zrobic single pass ze slownikiem cnt i potem sinle pass po slowniku 
        # ale czy to nie jest za proste no niby o(n) ale tez o(n) space, mysle ze da sie o(1) space
        '''
        n = len(nums)
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        res =[]
        for num, times in d.items():
            if times > n//3:
                res.append(num)
        return res
        '''
        num1, num2 = None, None
        cnt1, cnt2 = 0, 0
        
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        ## teraz wiemy ze num1 i num2 wystepuja najczesciej pytanie czy co najmniej n//3 razy
        # wiec trzeba zrobic second passa zeby to sprawidzic 
        res = []
        n = len(nums)
        if num1 is not None and nums.count(num1) > n // 3:
            res.append(num1)
        if num2 is not None and num2 != num1 and nums.count(num2) > n // 3:
            res.append(num2)
            
        return res

