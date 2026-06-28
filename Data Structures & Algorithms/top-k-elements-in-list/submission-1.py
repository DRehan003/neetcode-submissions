class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = []
        count = {}

        for x in nums:
            count[x] = 1 + count.get(x,0)

        while k > 0:
            elements.append(max(count, key=count.get))
            del count[max(count, key=count.get)]
            k -= 1


        return elements
