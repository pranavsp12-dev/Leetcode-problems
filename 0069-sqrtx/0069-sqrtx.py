class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        val=0
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid<=x:
                val=mid
                l=mid+1
            else:
                r=mid-1
        return val
            

        