class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)

        capacity.sort(reverse = True)

        total = 0
        count = 0

        for i in capacity:
            if total < s:
                total += i
                count += 1
            else:
                break

        return count
