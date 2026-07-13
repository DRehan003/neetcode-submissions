class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # nest loop hashmaps, loop thorugh again and group same counts tg and return list of same value counts

        # 1. time complexitiy
        # 2. each char freq for each word
        # 3. no
        # 4. hashmap of (some similarity) : words
        # 5. find the same version for each word, then create/update count in hashmap

        # create hashmap
        hashmap = {}
        
        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(word)
            else:
                hashmap[tuple(count)] = [word]

        return list(hashmap.values())


