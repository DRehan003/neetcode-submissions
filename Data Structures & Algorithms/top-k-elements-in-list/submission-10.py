class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force: sort the arr, increase count until value changes, then append the count to a list. return max k elements

        # 1. time complexity constraint prevents sorting
        # 2. value
        # 3. yes. if seen before than just increase count. if not create new key with value set to 1
        # 4. hashmap
        # 5. need to know if the value exists in hashmap alr

        # create hashmap
        hashmap, freq = {}, []

        # for loop through arr
        for x in nums:
            # if seen b4 increase value by 1 else create new key set to 1
            hashmap[x] = hashmap.get(x, 0) + 1
            #  for loop through uniq
        
        while k > 0:
            maximum = 0
            y = 0
            for x in hashmap.keys():
                if hashmap[x] > maximum:
                    maximum = hashmap[x]
                    y = x
            freq.append(y)
            del(hashmap[y])
            k -= 1

        return freq
                
                
                

        
        # return list
