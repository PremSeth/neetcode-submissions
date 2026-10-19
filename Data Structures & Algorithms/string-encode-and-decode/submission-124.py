class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for i in strs:
            encoded_strs.append(str(len(i)) + "#")
            encoded_strs.append(i)
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        pointer = 0
        decoded_strs = []
        num = []
        while pointer < len(s): 
            if not s[pointer] == "#":
                num.append(s[pointer])
                pointer +=1
            else: 
                word_length = int("".join(num))
                num = []
                decoded_strs.append(s[pointer+1:pointer+1+word_length])
                pointer +=1+word_length
        return decoded_strs