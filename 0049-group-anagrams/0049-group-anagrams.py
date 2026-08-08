class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for words in strs:
            word=''.join(sorted(words))

            if word in group:
                group[word].append(words)
            else:
                group[word]=[words]
        return list(group.values())

        