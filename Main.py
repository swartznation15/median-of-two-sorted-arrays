#0ms 100% solution to leet code problem
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        finalArray = sorted(nums1+nums2)
        mid = len(finalArray)/2
        return float(finalArray[mid] if len(finalArray)%2 else float(finalArray[mid-1] + finalArray[mid])/2)

   
