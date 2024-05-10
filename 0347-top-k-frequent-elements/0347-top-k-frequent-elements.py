class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in cnt:
                cnt[nums[i]] = 1
            else:
                cnt[nums[i]] += 1
        res = sorted(cnt.items(),  key=lambda x:x[1], reverse=True)
        x = []
        for i in res:
            x.append(i[0])

        return x[:k]
        