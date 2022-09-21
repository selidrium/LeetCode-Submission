class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits=''.join(map(str, digits))
        integer_digits=int(string_digits)+1
        digits=[]
        for i in str(integer_digits):
            digits.append(i)
            
        return digits