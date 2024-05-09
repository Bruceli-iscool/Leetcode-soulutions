class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = -1
        for z in nums:
            i = i + 1
            j = -1
            for y in nums:
                j = j + 1
                k = z + y
                if k == target:
                    if i != j:
                        return [i, j]
