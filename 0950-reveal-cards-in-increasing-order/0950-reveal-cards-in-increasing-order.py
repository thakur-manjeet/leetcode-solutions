from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deck=deque(deck)
        n=len(deck)
        result=[0]*n
        positions=deque(range(n))

        for card in deck:
            available_index=positions.popleft()
            result[available_index]=card

            if positions:
                x=positions.popleft()
                positions.append(x)
        return result        