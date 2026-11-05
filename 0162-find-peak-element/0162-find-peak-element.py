class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l=0
        n=len(nums)
        r=n-1
        while l<=n:
            mid=l+(r-l)//2
            leftval=nums[mid-1] if mid>0 else float('-inf')
            rightval=nums[mid+1] if mid<n-1 else float('-inf')
            if nums[mid]>leftval and nums[mid]>rightval:
                return mid
            elif nums[mid]>leftval and nums[mid]<rightval:
                l=mid+1
            else:
                r=mid-1
                