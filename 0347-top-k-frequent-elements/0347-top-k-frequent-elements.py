class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        freq2=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(freq2[i][0])
        return ans