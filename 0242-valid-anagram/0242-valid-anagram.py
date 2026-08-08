class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            freq[idx]+=1
        for ch in t:
            idx=ord(ch)-ord('a')
            freq[idx]-=1
        for i in range(len(freq)):
            if freq[i]!=0:
                return False
        return True
        