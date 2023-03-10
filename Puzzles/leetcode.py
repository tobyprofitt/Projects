class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_length = len(nums1) + len(nums2)
        i = 0
        j = 0
        current1 = nums1[i]
        current2 = nums2[j]
        if total_length%2 == 1:
            while i+j+2 < 1 + total_length/2:
                print(i, j, current1, current2)
                if j == len(nums2)-1:
                    i += 1
                    try:
                        current1 = nums1[i]
                    except IndexError as e:
                        i += 1
                if i == len(nums1)-1:
                    j += 1
                    try:
                        current2 = nums2[j]
                    except IndexError as e:
                        j += 1
                if current1 < current2:
                    i += 1
                    try:
                        current1 = nums1[i]
                    except IndexError as e:
                        i += 1
                else:
                    j += 1
                    try:
                        current2 = nums2[j]
                    except IndexError as e:
                        j += 1
            return float(min(current1, current2))
        else:
            while i+j+2 < 1 + total_length/2:
                print(i, j, current1, current2)
                if j == len(nums2)-1:
                    i += 1
                    try:
                        current1 = nums1[i]
                    except IndexError as e:
                        i += 1
                if i == len(nums1)-1:
                    j += 1
                    try:
                        current2 = nums2[j]
                    except IndexError as e:
                        j += 1
                if current1 < current2:
                    i += 1
                    try:
                        current1 = nums1[i]
                    except IndexError as e:
                        i += 1
                else:
                    j += 1
                    try:
                        current2 = nums2[j]
                    except IndexError as e:
                        j += 1
            return float(current1 + current2)/2
if __name__ == "__main__":
    # test Solution with test cases
    s = Solution()
    #print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 3], [2, 4]))