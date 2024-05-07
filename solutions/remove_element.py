class Solution(object):
    def removeElement(self, nums, val):
        while True:
            if val in nums:
                nums.remove(val)
            else: 
                break
        
