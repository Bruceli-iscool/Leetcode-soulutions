class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        l = len(happiness) - 1
        i = 0
        x = 0
        while i < k:
            x = x + max(happiness[l - i] - i, 0)
            i = i + 1
        return x
