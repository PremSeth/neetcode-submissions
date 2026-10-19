class Solution:
    size = []
    def encode(self, strs: List[str]) -> str:
        combine = []
        self.size = []
        val = []
        for i in strs: 
            self.size.append(len(i))
        return "#".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        clean = []
        first = 0
        for i in self.size: 
            clean.append(s[first:first+i])
            first += i+1
        return clean