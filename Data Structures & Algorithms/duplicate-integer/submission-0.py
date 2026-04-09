class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated = False
        numbers = set()
        for num in nums:
            if num in numbers:
                repeated = True
            numbers.add(num)
        return repeated
            