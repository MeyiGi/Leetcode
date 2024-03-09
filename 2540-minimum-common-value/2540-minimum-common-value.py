class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        nums1.append(0)
        nums2.append(0)

        while nums1[left] != 0 and nums2[right] != 0:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        
        return -1