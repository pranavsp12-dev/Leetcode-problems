class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                val=board[i][j]
                if val==".":
                    continue
                elif val in s:
                    return False
                else:
                    s.add(val)
        for i in range(9):
            s2=set()
            for j in range(9):
                val=board[j][i]
                if val==".":
                    continue
                elif val in s2:
                      return False
                else:
                    s2.add(val)
        for i in range(0,9,3):
            for j in range(0,9,3):
                s=set()
                for p in range(i,i+3):
                    for q in range(j,j+3):
                        val=board[p][q]
                        if val==".":
                            continue
                        elif val in s:
                            return False
                        else:
                            s.add(val)
        return True