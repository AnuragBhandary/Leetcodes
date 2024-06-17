class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        k = 0
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                seen.insert(0, nums[i])
            elif nums[i] == -1 and nums[i-1] == -1:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
            elif nums[i] == -1:
                k = 1
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)

        return ans
