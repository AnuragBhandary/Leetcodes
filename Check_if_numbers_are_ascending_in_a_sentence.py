class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        sentence = s.split()
        res = []

        for i in sentence:
            if i.isdigit():
                res.append(int(i))

        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False

        return True
