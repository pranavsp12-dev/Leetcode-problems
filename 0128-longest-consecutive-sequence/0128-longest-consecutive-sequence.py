class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
       
        longest=0
        if len(nums)==0:
            return 0
        for x in s:
            if x-1 not in s:
                count=1
                while x+1 in s:
                    x+=1
                    count+=1
                longest=max(count,longest)
        return longest

        