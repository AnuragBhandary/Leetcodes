class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cardset = set(fronts+backs)

        for f,b in zip(fronts, backs):
            if f == b:
                cardset.discard(f)

        return min(cardset, default = 0)
