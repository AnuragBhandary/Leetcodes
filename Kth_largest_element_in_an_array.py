class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minval = min(nums)
        maxval = max(nums)

        count = [0] * (maxval - minval + 1)

        for num in nums:
            count[num - minval] += 1

        remain = k

        for num in range(len(count)-1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + minval
