class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        minVal, maxVal = min(nums), max(nums)

        for val in nums:
            counts[val] += 1

        index = 0

        for val in range(minVal, maxVal + 1):
            while counts[val] > 0:
                nums[index] = val
                index += 1
                counts[val] -= 1

        return nums
