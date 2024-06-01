class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        i1 = nums1.intersection(nums2)
        i2 = nums2.intersection(nums3)
        i3 = nums3.intersection(nums1)

        res = list(i1.union(i2, i3))

        return res
