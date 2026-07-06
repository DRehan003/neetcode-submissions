class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest consecutive sequence of 1 incrementing elements
        # must be O(n) - core constraint
        # 2. if x - 1 in hashset
        # 3. none
        # 4. hashset
    

        # create sequence var
        seq = 0

        # loop through the hashset elements
        for x in nums:
            # check if x - 1 is in the hashset
            if x - 1 in nums:
            # if it does then it is not the start of a seq,
                continue
            # if it doesn't then it is a start of a seq
            else:
                counter = 1
                checking = True
                while checking == True:
                    # check if x + counter is in hashset
                    if x + counter in nums:
                        counter += 1
                    # if not
                    else:
                        # check if counter > seq:
                        if counter > seq:
                            seq = counter
                        checking = False
            
        return seq