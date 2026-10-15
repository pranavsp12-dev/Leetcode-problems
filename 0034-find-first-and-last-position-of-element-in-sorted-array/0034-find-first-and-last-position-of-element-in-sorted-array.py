class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        if n == 0:
           return [-1, -1]

        l = 0
        r = n - 1
        first = -1

        while l <= r:
             k = l + (r - l) // 2

             if nums[k] == target:
                 first = k
                 r = k - 1
             elif nums[k] > target:
                   r = k - 1
             else:
                  l = k + 1

        l = 0
        r = n - 1
        last = -1

        while l <= r:
            k = l + (r - l) // 2

            if nums[k] == target:
                last = k
                l = k + 1
            elif nums[k] > target:
                r = k - 1
            else:
               l = k + 1
        return [first,last]
        
        
        
        
        