class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            k=l+(r-l)//2
            if nums[k]==target:
                return k
            elif nums[k]<target:
                  l=k+1
            else:
                r=k-1
        return l
        