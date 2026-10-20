class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        l=0
        r=m*n-1
        while l<=r:
            mid=l+(r-l)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                r=mid-1
            else:
                l=mid+1
        return False