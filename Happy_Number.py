''' SAW THE SOLUTION '''

class Solution:
    def isHappy(self, n: int) -> bool:
        ref = set()
        while True:
            Sum = 0
            while n > 0:
                i = n % 10
                Sum += (i * i)
                n = n // 10
            
            if Sum == 1:
                return True
            elif Sum in ref:
                return False
            else:
                ref.add(Sum)
                n = Sum

''' SOLVED 343/420 TEST CASES
--------------------------------
class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        count = 0
        ref = set()
        
        while count in range(1000):
            sum = 0
            while i<1:
                num = list(str(n))
                number = [int(i) for i in num]
                i+=2
            number = [int(i) for i in num]
            for j in number:
                sum += i**2
            print(sum)
            if sum == 1:
                return True
            if sum not in ref:
                ref.add(sum)
            else:
                return False
            num = list(str(sum))
            count += 1
'''
