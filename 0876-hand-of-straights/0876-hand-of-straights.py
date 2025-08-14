
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        count = Counter(hand)

        for card in hand:
            if count[card] == 0:
                continue
            for x in range(card, card + groupSize):
                if count[x] == 0:
                    return False
                count[x] -= 1
        return True
