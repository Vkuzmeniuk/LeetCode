class Solution:
    def minNumber(self, nums1, nums2) -> int:
        check = any(item in nums1 for item in nums2)
        if check:
            matched = set(nums1).intersection(set(nums2))
            value = list(sorted(matched))
            return value[0]
        else:
            nums1 = min(nums1)
            nums2 = min(nums2)
            if nums1 == nums2:
                return nums1
            else:
                new_list = [nums1, nums2]
                srt_new_lst = sorted(new_list)
                return int(f"{srt_new_lst[0]}{srt_new_lst[1]}")
        
if __name__ == "__main__":
    sol = Solution()
    list1 = [5,8,2,7]
    list2 = [5,2,8,4,7,1,3]
    print(sol.minNumber(list1, list2))