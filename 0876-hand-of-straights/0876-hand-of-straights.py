#nlogn, becouse of sorting
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand) # to jest slownik mowiacy ile razy cos wystepuje
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
        '''
#O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]: # here we look for the start of sequence
                start -= 1
            while start <= num:
                while count[start]: # here we just go like in the nlogn approach
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True