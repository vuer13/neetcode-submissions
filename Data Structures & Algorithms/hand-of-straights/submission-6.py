class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1
        hand.sort()

        for num in hand:
            if count[num] > 0:
                for i in range(num, num + groupSize):
                    if count.get(i, 0) == 0:
                        return False
                    count[i] -= 1
                
        return True
