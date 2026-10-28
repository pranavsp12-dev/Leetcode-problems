class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        l=0
        r=len(mat[0])-1
        while l<=r:
            mid=(l+r)//2
            maxrow=0
            for i in range(len(mat)):
                if mat[i][mid]>mat[maxrow][mid]:
                    maxrow=i
            maxval=mat[maxrow][mid]
            leftval=mat[maxrow][mid-1] if mid>0 else -1
            rightval=mat[maxrow][mid+1] if mid<len(mat[0])-1 else -1
            if maxval>leftval and maxval>rightval:
                return [maxrow,mid]
            elif maxval>leftval and maxval<rightval:
                l=mid+1
            else:
                r=mid-1
        


        