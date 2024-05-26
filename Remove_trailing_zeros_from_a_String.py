class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        number = list(num)
        print(number)

        for i in range(len(number)):
            if number[-1] == "0":
                number.pop()

        return("".join(number))
