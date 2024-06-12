# Ok let's try Neet approach, see if it's less fragile to out-of-bounds edge cases
# 80% runtime, 75% memory
# Sigh this question is still ridiculous after watching Neet, even if I have the intuition the out of bounds edge cases are just...
class Solution_AfterNeet(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        partition_size = total_len // 2
        # Ensure nums1 is pointing to smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1        

        # Find L) parititon of nums1, such that when added with L) partition of nums2, will get left parititon of merged array
        l, r = 0, len(nums1) - 1

        while True:
            nums1_L_i = (l + r) // 2
            nums2_L_i = partition_size - nums1_L_i - 2
            print(nums1_L_i, nums2_L_i)
            nums1_l_max = nums1[nums1_L_i] if nums1_L_i >= 0 else float("-infinity")
            nums2_l_max = nums2[nums2_L_i] if nums2_L_i >= 0 else float("-infinity")
            nums1_r_min = nums1[nums1_L_i + 1] if nums1_L_i + 1 < len(nums1) else float("infinity")
            nums2_r_min = nums2[nums2_L_i + 1] if nums2_L_i + 1 < len(nums2) else float("infinity")

            if nums1_l_max <= nums2_r_min and nums2_l_max <= nums1_r_min:
                if total_len % 2 == 1: return min(nums1_r_min, nums2_r_min)
                else: return (min(nums1_r_min, nums2_r_min) + max(nums1_l_max, nums2_l_max)) / 2.0
            elif nums2_l_max > nums1_r_min:
                l = nums1_L_i + 1
            else:
                r = nums1_L_i - 1

# 33% runtime, 14% memory
# Even when I had the main concept of the hint, so many out-of-bounds edge cases urgh. Must be an easier way.
class Solution_V2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        target_l = (total_len - 1) // 2
        target_r = target_l
        if total_len % 2 == 0: target_r += 1
        
        # Escape cases - O(1) solution
        if len(nums1) == 0:
            if target_l == target_r: return nums2[target_l]
            else: return (nums2[target_l] + nums2[target_r]) / 2.0
        if len(nums2) == 0:
            if target_l == target_r: return nums1[target_l]
            else: return (nums1[target_l] + nums1[target_r]) / 2.0

        l1, l2 = 0, 0
        k = target_l
        while k > 0:
            # num_to_cut - round up
            num_to_cut = k // 2
            if k % 2 == 1: num_to_cut += 1
            # Out of bounds check
            if l1 >= len(nums1):
                l2 = l2 + num_to_cut
            elif l2 >= len(nums2):
                l1 = l1 + num_to_cut
            else:
                # Cannot cut more than entire arr 
                num_to_cut = min(num_to_cut, len(nums1) - l1, len(nums2) - l2)            
                if nums1[l1 + num_to_cut - 1] < nums2[l2 + num_to_cut - 1]:
                    l1 = l1 + num_to_cut
                else:
                    l2 = l2 + num_to_cut
            k -= num_to_cut

        if l1 >= len(nums1):
            target_l_num = nums2[l2]
        elif l2 >= len(nums2):
            target_l_num = nums1[l1]
        else:
            if nums1[l1] < nums2[l2]:
                target_l_num = nums1[l1]
            else:
                target_l_num = nums2[l2]
        if target_l == target_r: return target_l_num

        # Find target_r
        l1, l2 = 0, 0
        k = target_r
        while k > 0:
            # num_to_cut - round up
            num_to_cut = k // 2
            if k % 2 == 1: num_to_cut += 1
            # Out of bounds check
            if l1 >= len(nums1):
                l2 = l2 + num_to_cut
            elif l2 >= len(nums2):
                l1 = l1 + num_to_cut
            else:
                # Cannot cut more than entire arr 
                num_to_cut = min(num_to_cut, len(nums1) - l1, len(nums2) - l2)            
                if nums1[l1 + num_to_cut - 1] < nums2[l2 + num_to_cut - 1]:
                    l1 = l1 + num_to_cut
                else:
                    l2 = l2 + num_to_cut
            k -= num_to_cut

        if l1 >= len(nums1):
            target_r_num = nums2[l2]
        elif l2 >= len(nums2):
            target_r_num = nums1[l1]
        else:
            if nums1[l1] < nums2[l2]:
                target_r_num = nums1[l1]
            else:
                target_r_num = nums2[l2]

        return (target_l_num + target_r_num) / 2.0

# Can brute force this in O((M+N) * lg (M+N)) by sorting
# I have a O(lg(M) * lg(N)) solution but I'm getting tripped up by the edge case of duplicate numbers mmm  
# And I spent 2+ hrs here already, without a passing implementation
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        target_l = (total_len - 1) // 2
        target_r = target_l
        if total_len % 2 == 0: target_r += 1
        target_l_num, target_r_num = None, None

        # Escape cases - O(1) solution
        if len(nums1) == 0:
            return (nums2[target_l] + nums2[target_r]) / 2.0
        if len(nums2) == 0:
            return (nums1[target_l] + nums1[target_r]) / 2.0
        
        # O(max(lg M, lg N)) subroutine
        def findRank(sortedArray, num):
            resp = 0
            l, r = 0, len(sortedArray) - 1
            while l <= r:
                mid = (l + r) // 2
                if sortedArray[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
                    resp = max(resp, mid + 1)
            return resp
        
        # Binary search nums1 for target_l
        l, r = 0, len(nums1) - 1

        while l <= r:
            mid = (l + r) // 2
            nums2_rank = findRank(nums2, nums1[mid])
            rank = mid + nums2_rank
            print(rank)
            if rank == target_l:
                target_l_num = nums1[mid]
                break
            elif rank < target_l:
                l = mid + 1
            else:
                r = mid - 1

        # If haven't found target_l, look in nums2:
        if not target_l_num:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = (l + r) // 2
                nums1_rank = findRank(nums1, nums2[mid])
                rank = mid + nums1_rank
                if rank == target_l:
                    target_l_num = nums2[mid]
                    break
                elif rank < target_l:
                    l = mid + 1
                else:
                    r = mid - 1

        if target_l == target_r: return target_l_num

        # Binary search nums1 for target_2
        l, r = 0, len(nums1) - 1

        while l <= r:
            mid = (l + r) // 2
            nums2_rank = findRank(nums2, nums1[mid])
            rank = mid + nums2_rank
            if rank == target_r:
                target_r_num = nums1[mid]
                break
            elif rank < target_r:
                l = mid + 1
            else:
                r = mid - 1

        # If haven't found target_l, look in nums2:
        if not target_r_num:
            l, r = 0, len(nums2) - 1
            while l <= r:
                mid = (l + r) // 2
                nums1_rank = findRank(nums1, nums2[mid])
                rank = mid + nums1_rank
                if rank == target_r:
                    target_r_num = nums2[mid]
                    break
                elif rank < target_r:
                    l = mid + 1
                else:
                    r = mid - 1

        return (target_l_num + target_r_num) / 2.0

sln = Solution_AfterNeet()
# print(sln.findMedianSortedArrays([1,2], [3,4])) #2.5
# print(sln.findMedianSortedArrays([1,2], [3])) #2
# print(sln.findMedianSortedArrays([1,2], [])) #1.5
# print(sln.findMedianSortedArrays([1,3,5,7], [2,4,6,8])) #4.5
# print(sln.findMedianSortedArrays([0,0], [0,0])) #0.0
# print(sln.findMedianSortedArrays([2,2,2,2], [2,2,2])) #2
# print(sln.findMedianSortedArrays([1,2], [1,2,3])) #2
# print(sln.findMedianSortedArrays([1], [2,3,4,5])) #3
# print(sln.findMedianSortedArrays([1], [2,3,4,5,6,7])) #4
# print(sln.findMedianSortedArrays([1], [2,3,4,5,6,7,8])) #4.5
# print(sln.findMedianSortedArrays([1,2], [-1,3])) #1.5
# print(sln.findMedianSortedArrays([2], []))
print(sln.findMedianSortedArrays([2,3,4,5,6], [1])) #3


