class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right: 
            num1 = numbers[left]
            num2 = numbers[right]
            val = num1+num2
            if val < target: 
                left +=1
            elif val > target: 
                right -=1
            else: 
                return [left+1, right+1]
        

        