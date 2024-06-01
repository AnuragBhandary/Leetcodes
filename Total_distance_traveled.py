class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        fuel = 0

        while mainTank//5 > 0 and additionalTank > 0:
            mainTank -= 4    #(-5 + 1 = -4)
            fuel += 5
            additionalTank -= 1

        fuel += mainTank
        fuel *= 10

        return fuel
