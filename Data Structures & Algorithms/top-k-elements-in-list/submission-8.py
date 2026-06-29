class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, switch = {}, {}

        for x in nums:
            freq[x] = 1 + freq.get(x, 0)

        for key, value in freq.items():
            if value in switch:
                switch[value].append(key)
            else:
                switch[value] = [key]

        count = []
        
        while k > 0:
            maxkey = max(switch.keys()) 
            for num in switch[maxkey]:
                count.append(num)
                k -= 1
                if k == 0:
                    break
            del switch[maxkey]
                
        return count