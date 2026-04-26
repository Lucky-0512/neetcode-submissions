class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, val in enumerate(nums):
            set_bit = target - val

            if set_bit in seen:
                return [seen[set_bit],i] # return it's complent and current index

            seen[val] = i # store that exactl compl

        return []



        