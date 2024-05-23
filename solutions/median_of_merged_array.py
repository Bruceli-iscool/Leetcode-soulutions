import statistics

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new = nums1 + nums2
        return statistics.median(new)
