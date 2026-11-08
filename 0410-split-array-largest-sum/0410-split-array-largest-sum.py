class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=(l+r)//2
            count=1
            cur_sum=0
            for i in nums:
                if cur_sum+i<=mid:
                    cur_sum+=i
                else:
                    count+=1
                    cur_sum=i
            if count<=k:
                r=mid
            else:
                l=mid+1
        return l