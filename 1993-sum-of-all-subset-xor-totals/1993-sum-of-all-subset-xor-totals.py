class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        # 2^n to wszystkie podzbiory zbioru n elementowego
        n = len(nums)

        def rek(cur_idx, cur_num):
            if cur_idx == n:
                return cur_num
            # include
            include = rek(cur_idx + 1, cur_num^nums[cur_idx])
            # dont include
            not_include = rek(cur_idx + 1, cur_num)

            return include + not_include
        
        # cur_num initialyy 0 beacouse 0^num = num
        return rek(0, 0)