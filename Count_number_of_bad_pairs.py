class Solution:
    def countBadPairs(self, nums: List[int]) -> int:        
        diffcount = defaultdict(int)
        total_pairs = len(nums)* (len(nums) - 1) // 2
        good_pairs = 0

        for i, num in enumerate(nums):
            # In the question j-i = nums[j] - nums[i]
            # So j - nums[j] = i - nums[i]
            # Now it's easier, if i - nums[i] in diffcount, then it's a good pair
            diff = i - num   
            if diff in diffcount:
                good_pairs += diffcount[diff]
            diffcount[diff] += 1

        bad_pairs = total_pairs - good_pairs

        return bad_pairs
        
        
        '''O(n^2) (Exceeded time limit)'''
        # count = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if j - i != nums[j] - nums[i]:
        #             count += 1

        # return count
