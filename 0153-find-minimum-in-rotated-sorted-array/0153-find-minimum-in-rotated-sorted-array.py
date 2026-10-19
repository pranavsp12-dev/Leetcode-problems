class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0
        r=l+1
        n=len(nums)
        min=nums[l]
        while(l<=r and r<=n-1):
            if nums[l]>=nums[r]:
                if min<nums[r]:
                    return min
                else:
                    return nums[r]
            else:
                l=l+1
                r=l+1
        return min