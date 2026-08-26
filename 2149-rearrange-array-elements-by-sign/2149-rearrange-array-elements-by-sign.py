class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        temp=[0]*len(nums)
        l=0
        r=1
        # while(nums[r]<0):
        #     r+=1
        # temp.append(nums[r])
        for i in range(0,len(nums)):
            if nums[i]>0:
                temp[l]=nums[i]
                l+=2
            else:
                temp[r]=nums[i]
                r+=2
        return temp

        