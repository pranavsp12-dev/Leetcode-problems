class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        arr=[]
        for i in range(numRows):
            row=[1]
            if i>0:
                for j in range(len(arr[i-1])-1):
                    row.append(arr[i-1][j]+arr[i-1][j+1])
                row.append(1)
            arr.append(row)
        return arr


            

        