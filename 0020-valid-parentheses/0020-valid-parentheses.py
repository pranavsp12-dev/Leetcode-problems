class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        if len(s)==0:
            return True
        for r in range(len(s)):
            if s[r]=='(' or s[r]=='{' or s[r]=='[':
                lst.append(s[r])
            else:
                if not lst:
                    return False
                x=lst.pop()
                if s[r]==')' and x!='(':
                    return False
                elif s[r]=='}' and x!='{':
                    return False
                elif s[r]==']' and x!='[':
                    return False
                else:
                   continue
                    
        if len(lst)==0:
            return True
        return False
       
        
        