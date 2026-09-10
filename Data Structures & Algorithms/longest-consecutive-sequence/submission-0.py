class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numsSet:
                consecutive = 1
                while (num + consecutive) in numsSet:
                    consecutive += 1
                longest = max(consecutive, longest)
            
        return longest