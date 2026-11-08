class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0
        result=""
        for ch in s:
            if ch=='(':
               if d>0:
                  result+=ch
               d+=1
            else:
                d-=1
                if d>0:
                    result+=ch
        return result
        
        