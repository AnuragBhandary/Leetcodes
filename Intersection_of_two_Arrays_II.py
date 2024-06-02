class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}

        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1

        for i in nums1:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        k = 0

        for i in nums2:
            if i in res and res[i]>0:
                nums1[k] = i
                k += 1
                res[i] -= 1

        return nums1[:k]

        
        # Beat 99.8% in memory (although very slow comparatively)
        '''
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))

        return res
        '''
