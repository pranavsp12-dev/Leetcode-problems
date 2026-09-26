class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        arr=[]
        for i in range(rowIndex+1):
            row=[1]
            if i>0:
                for j in range(len(arr[i-1])-1):
                    row.append(arr[i-1][j]+arr[i-1][j+1])
                row.append(1)
            arr.append(row)
        return arr[rowIndex]

