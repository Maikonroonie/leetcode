class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lenght = None
        for num in nums:
            if num == 1:
                if lenght is not None and  lenght < k:
                    return False
                lenght = 0
            elif lenght is not None:
                lenght +=1

        return True