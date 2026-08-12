class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=set()
        maxlen=0
        left=0
        for right in range(len(s)):
            while s[right] in longest:
                longest.remove(s[left])
                left=left+1
            longest.add(s[right])
            maxlen=max(maxlen,len(longest))
        return maxlen
        

            
        