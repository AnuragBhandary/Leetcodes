class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        '''TWO POINTER'''
        x = 0
        y = 0

        l1 = len(nums1)
        l2 = len(nums2)

        while x < l1 and y < l2:
            if nums1[x] == nums2[y]:
                return nums1[x]
            elif nums1[x] < nums2[y]:
                x += 1
            else:
                y += 1

        return -1



        # set1 = set(nums1)
        # set2 = set(nums2)

        # common = set1.intersection(set2)

        # if common:
        #     return min(common)
        # else:
        #     return -1
        
        
        # set1 = set(nums1)
        
        # for x in nums2:
        #     if x in set1:
        #         return x

        # return -1
