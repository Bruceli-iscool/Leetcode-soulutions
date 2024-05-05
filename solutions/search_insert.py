class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            z = nums
            x = -1
            for h in range(len(nums)):
                x = x + 1
                y = z[0]
                if y == target:
                    return x
                else:
                    z.pop(0)
        else:
            nums.append(target)
            nums.sort()
            z = nums
            x = -1
            for h in range(len(nums)):
                x = x + 1
                y = z[0]
                if y == target:
                    return x
                else:
                    z.pop(0)