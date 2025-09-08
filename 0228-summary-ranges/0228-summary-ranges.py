class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return []
        start = prev = nums[0]

        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                if start == prev:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{prev}")
                start = prev = num

        # domknij ostatni przedział
        if start == prev:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{prev}")

        return res
            