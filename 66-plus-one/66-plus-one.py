class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = [str(char) for char in digits]
        str2 = ""
        for char in str1:
            str2+= char
        str3 = int(str2)
        number = str3 + 1
        str4 = str(number)
        digits = [num for num in str4]
        return (digits)