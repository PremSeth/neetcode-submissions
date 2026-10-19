class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            value = "".join(sorted(i))
            if value in seen: 
                seen[value].append(i)
            else: 
                seen[value] = [i]
        return list(seen.values())
