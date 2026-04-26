class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        dup_list = []
        for i in nums:
            if i in dup_list:
                dup = True
                return dup
            else:
                dup_list.append(i)

        return dup

                


        