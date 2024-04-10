class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)

        deck.sort()
        result = [0 for _ in deck]
        for card in deck:
            result[queue.popleft()] = card

            if queue:
                queue.append(queue.popleft())
        return result