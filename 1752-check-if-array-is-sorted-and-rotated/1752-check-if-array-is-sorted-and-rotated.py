class Solution:
    def check(self, nums: List[int]) -> bool:
        num_sorted=nums.copy()
        count=0
        for i in range(len(nums)):
            idx=(i+1)%len(nums)
            if nums[i]>nums[idx]:
                count+=1
        if count>1:
            return False
        else:
            return True
        