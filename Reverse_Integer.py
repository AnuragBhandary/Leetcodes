class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        rev = list(reversed(num))
        if rev[-1] == "-":
            rev.pop()
            rev.insert(0, "-")
        res = "".join(rev)

        if int(res) not in range(-2**31, 2**31):
            return 0

        return int(res)
