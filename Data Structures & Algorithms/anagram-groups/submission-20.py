class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        chars = [0]*26
        for i in strs: 
            for c in i: 
                chars[ord(c) - ord("a")] +=1
            result[tuple(chars)].append(i)
            chars = [0]*26
        return list(result.values())
                