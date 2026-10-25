class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            time=0
            for i in piles:
                time+=(i+mid-1)//mid
            if time<=h:
                r=mid #because the mid might be the min speed as well
            else:
                l=mid+1
        return l

            

        
        