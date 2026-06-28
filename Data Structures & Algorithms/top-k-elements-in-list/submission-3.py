class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        e = [[] for i in range(len(nums) + 1)]
        ## e = [[] * len(nums)]

        for x in nums:
            count[x] = 1 + count.get(x, 0)

        for key, value in count.items():
            e[value].append(key)

        result = []
        for i in range(len(e) -1, 0, -1):
            for n in e[i]:
                result.append(n)
            if len(result) == k:
                return result