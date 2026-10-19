class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
    
        n=len(nums)
        r=n-1
        id=-1
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<=nums[mid]:
                if target>=nums[l] and target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                   if target>nums[mid] and target<=nums[r]:
                        l=mid+1
                   else:
                        r=mid-1

        return id
            
            
