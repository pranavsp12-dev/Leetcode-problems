class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0]) #col
        m=len(matrix) #row
        l=0
        r=n-1
        while l<len(matrix) and r>=0:
            x=matrix[l][r]
            if x==target:
                return True
            elif x>target:
                r-=1
            else:
                l+=1
        return False
            
        return False
        