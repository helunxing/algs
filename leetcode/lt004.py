class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A
        half = (m+n+1)//2
        le, ri = 0, m
        while le <= ri:
            mi = (le+ri)//2
            mj = half-mi
            if 0 < mi and A[mi-1] > B[mj]:
                ri = mi-1
            elif mi < m and B[mj-1] > A[mi]:
                le = mi+1
            else:
                break
            # valid = True & (A[mi-1] < B[mj] if 0 < mi else True) & \
            #     (B[mj-1] < A[mi] if mi < m else True)

        if mi > 0 and mj > 0:
            l_max = max(A[mi-1], B[mj-1])
        elif mi == 0:
            l_max = B[mj-1]
        elif mj == 0:
            l_max = A[mi-1]

        if (m+n) & 1:
            return l_max

        if mi < m and mj < n:
            r_min = min(A[mi], B[mj])
        elif mi >= m:
            r_min = B[mj]
        elif mj >= n:
            r_min = A[mi]
        return (l_max+r_min)/2


s = Solution()
# print(s.findMedianSortedArrays([1], [2]))
# print(s.findMedianSortedArrays([3], [-2, -1]))
# print(s.findMedianSortedArrays([], [2, 3]))
print(s.findMedianSortedArrays([1, 3], [2]))
# print(s.findMedianSortedArrays([1, 2], [3, 4]))
# print(s.findMedianSortedArrays([1], [1]))


# [1]
# [2]
# []
# [2, 3]
# [1, 3]
# [2]
# [1, 2]
# [3, 4]
# [1]
# [1]

class Solution_fail:
    # 此问题与两个数组中第（m+n）/2 +1大的元素相同
    # 先做704二分查找。744左搜索
    def findMedianSortedArrays(self, nums1, nums2):
        def sest_ger_tn_tar(nums, l, r, tar):
            if not nums:
                return 0
            if nums[r] < tar:
                return r+1
                #  or tar < nums[0]
            while l < r:
                m = l+(r-l)//2
                if tar <= nums[m]:
                    r = m
                else:
                    l = m+1
            return r

        m, n = len(nums1), len(nums2)
        odd = (m+n) & 1 == 1

        if not nums1 or not nums2:
            if odd:
                return nums1[m//2] if nums1 else nums2[n//2]
            else:
                return (nums1[m//2]+nums1[m//2-1])/2 if nums1 \
                    else (nums2[m//2]+nums2[m//2-1])/2
        if m == n == 1 and nums1[0] == nums2[0]:
            return nums1[0]
        l1, r1 = 0, m-1
        l2, r2 = 0, n-1
        tar_serN = (m+n)//2

        while True:
            m1, m2 = l1+(r1-l1)//2, l2+(r2-l2)//2
            _2c1 = sest_ger_tn_tar(nums2, l2, r2, nums1[m1])
            # nums2中比m1小的最大的数的下标
            _1c2 = sest_ger_tn_tar(nums1, l1, r1, nums2[m2])
            # nums1中比m2小的最大的数的下标
            if m1+_2c1 < tar_serN:
                l1 = m1+1
            elif tar_serN < m1+_2c1:
                r1 = m1-1
            else:
                ans = nums1[m1]
                break
            if m2+_1c2 < tar_serN:
                l2 = m2+1
            elif tar_serN < m2+_1c2:
                r2 = m2-1
            else:
                ans = nums2[m2]
                break

        if not odd:
            _1 = sest_ger_tn_tar(nums1, 0, m-1, ans)
            _2 = sest_ger_tn_tar(nums2, 0, n-1, ans)

            ans2 = nums1[_1-1 if _1 else 0]
            if _2:
                ans2 = max(ans2, nums2[_2-1])
            ans = (ans+ans2)/2

        return ans
