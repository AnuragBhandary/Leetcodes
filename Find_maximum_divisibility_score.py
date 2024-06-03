class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # SAW SOLUTION
        res = 0 
        count = -1
        for d in divisors:
            curr = sum(1 for i in nums if i%d == 0)
            if curr > count:
                count = curr
                res = d
            elif curr == count:
                res = min(res, d)
        return res
        
        ''' Solved 154/157 test cases, didn't solve the last 3 for some reason even though the answer was correct.'''
        # res = {}

        # for i in range(len(divisors)):
        #     res[divisors[i]] = 0

        # for i in range(len(divisors)):
        #     for j in range(len(nums)):
        #         if nums[j]%divisors[i] == 0:
        #             res[divisors[i]] += 1

        # max_val = max(res.values())

        # print([key for key, value in res.items() if value == max_val])

        # return min(key for key, value in res.items() if value == max_val)

        # print(res)
