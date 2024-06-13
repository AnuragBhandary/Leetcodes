class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total = 0

        for i,j in zip(students, seats):
            total += abs(i-j)

        return total
