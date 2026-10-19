class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs: 
            seen.setdefault("".join(sorted(i)), []).append(i)
        submission = []
        for i,j in seen.items():
            submission.append(j)
        return submission
        