class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            cursum=max(cursum+nums[i],nums[i])
            maxsum=max(maxsum,cursum)

    
        return maxsum
        #kadane's algo- if the sum is less then the current element then start the subarray from this new element. else just keep on adding to find the sum.