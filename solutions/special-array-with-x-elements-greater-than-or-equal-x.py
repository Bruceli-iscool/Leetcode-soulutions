class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for c in range(1, 1001):
            y = 0
            for z in nums:
                if c <= z:
                    y = y + 1
            if y == c:
                return y
        return -1
