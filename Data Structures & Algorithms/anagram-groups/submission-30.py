class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for letter in i: 
                count[ord(letter) - ord('a')] +=1
            seen[tuple(count)].append(i)
        return list(seen.values())
