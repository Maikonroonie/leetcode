class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        maximum = nums[0]
        minimum = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Gdy liczba jest ujemna, zamieniamy minimum i maximum
            if num < 0:
                maximum, minimum = minimum, maximum

            maximum = max(num, maximum * num)
            minimum = min(num, minimum * num)

            result = max(result, maximum)

        return result
        def dynamic_approach(self, nums):
            n = len(nums)
            if n == 0:
                return 0

            dp_max = [0] * n # dp_max[i] maksymalny iloczyn podciagu konczacy sie na pozycji i
            dp_min = [0] * n# dp_min[i] minimalny iloczyn podciagy konczacyu sie na pozycji i 

            dp_max[0] = nums[0]
            dp_min[0] = nums[0]
            result = nums[0]

            for i in range(1, n):
                dp_max[i] = max(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
                dp_min[i] = min(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])

                result = max(result, dp_max[i])

            return result

