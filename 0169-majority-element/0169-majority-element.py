import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        res=n//2
        d={}
        for i in range(n):
            d[nums[i]]=d.get(nums[i],0)+1
        dict_sort=dict(sorted(d.items() , key=lambda item:item[1],reverse=True))
        first_key=next(iter(dict_sort))
        return first_key
        
        