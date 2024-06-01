class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        amount = 100 - purchaseAmount

        if 0 <= amount%10 <= 5:
            amount = amount - amount%10
        elif 6 <= amount%10 <= 9:
            amount = amount + (10 - amount%10)

        return amount
