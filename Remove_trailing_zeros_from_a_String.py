class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        number = list(num)
        for i in range(len(number)):
            if number[-1] == "0":
                number.pop()
            elif number[-1] != "0":
                return("".join(number))
        

        #return str(int(num[::-1]))[::-1]
