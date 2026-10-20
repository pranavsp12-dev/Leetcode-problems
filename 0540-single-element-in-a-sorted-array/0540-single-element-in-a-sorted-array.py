class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        r=n-1
        #count=0
        
        while l<r:
         mid=l+(r-l)//2
         if mid%2==1:
            mid-=1
         if nums[mid]==nums[mid+1]:
            l=mid+2
         else:
            r=mid
        return nums[l]

        
        


            
            
        