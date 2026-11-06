class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        arr=sorted(nums1+nums2)
        l=0
        n=len(arr)
        r=n-1
        mid=(l+r)//2
        med=0
        if n%2==0:
            x=arr[mid]+arr[mid+1]
            med=x/2
        else:
            med=arr[mid]
        return med
