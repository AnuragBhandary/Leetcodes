class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, sub_sum, count = 0, 0, 0

        for right in range(len(arr)):

            # close window
            if right - left + 1 > k:
                sub_sum -= arr[left]
                left += 1

            # open window
            sub_sum += arr[right]
            if right - left + 1 == k and sub_sum/k >= threshold:
                count += 1
            
        return count
        
        
        '''MY SOLUTION DIDN'T WORK (SOLVED 68/69 TEST CASES)'''
        # count = 0
        # add = 0
        # l = len(arr)+1-k

        # for i in range(l):
            
        #     # DIDN'T WORK, 68/69 CASES
        #     # for j in range(k):
        #     #     add += arr[i]
        #     #     i += 1
        #     # if add/k >= threshold:
        #     #     count += 1
        #     # add = 0

        #     # SAME WITH THIS, 68/69 CASES
        #     # if sum(arr[i:i+k])/k >= threshold:
        #     #     count += 1

        # return count
