class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 1
        suf = 1
        for i in range(len(nums)):
            ans.append(pre)
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suf
            suf *= nums[i]
        return ans

  



