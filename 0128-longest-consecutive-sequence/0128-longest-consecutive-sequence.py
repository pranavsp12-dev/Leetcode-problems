class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     maxlen=0
     count=0
     n=len(nums)
     if n==0:
        return 0
     nums.sort()
     for i in range(n-1):
        if nums[i+1]==nums[i]+1 :
            count+=1
        elif nums[i+1]==nums[i]:
            continue
           
        else:
            maxlen=max(count,maxlen)
            count=0
        
        
     return max(maxlen,count)+1
       
        