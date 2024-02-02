class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Dictionary of roman numerals
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        # Length of the given string
        n = len(s)

        # This will store the result
        num = roman_dict[s[n-1]]

        # Loop for each character from right to left
        for i in range(n-2, -1, -1):
            if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                num += roman_dict[s[i]]
            else:
                num -= roman_dict[s[i]] 
        return num





        

        