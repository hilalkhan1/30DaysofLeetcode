class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = set()
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            j, k = i + 1, n - 1
            while j < k:
                p_list = [nums[i], nums[j], nums[k]]
                t_sum = sum(p_list)

                if t_sum == 0:
                    final_list.add(tuple(p_list))
                    j, k = j+1, k-1
                elif t_sum > 0:
                    k -=1
                elif t_sum < 0:
                    j += 1

        return final_list
                    

        