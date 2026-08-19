class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            smaller = nums2
            larger = nums1
        else:
            smaller = nums1
            larger = nums2

        total_length = len(smaller) + len(larger)

        low = 0
        high = len(smaller)

        while low <= high:
            partition_X = (low + high) // 2
            partition_Y = (total_length + 1) // 2 - partition_X
            if partition_X == 0:
                l1 = float('-inf')
            else:
                l1 = smaller[partition_X - 1]
            if partition_X == len(smaller):
                r1 = float('inf')
            else:
                r1 = smaller[partition_X]
            if partition_Y == 0:
                l2 = float('-inf')
            else:
                l2 = larger[partition_Y - 1]
            if partition_Y == len(larger):
                r2 = float('inf')
            else:
                r2 = larger[partition_Y]
            if l1 <= r2 and l2 <= r1:

                if total_length % 2 == 0:
                    left_max = max(l1, l2)
                    right_min = min(r1, r2)
                    return (left_max + right_min) / 2.0
                else:
                    return float(max(l1, l2))

            elif l1 > r2:
                high = partition_X - 1
            else:
                low = partition_X + 1

        return 0.0
