class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumarate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            if n1 + n2> n2 + n1:
                return -1 #to return n1
            else:
                return 1 #to return n2
        sorted(nums, key=cmp_to_key(compare))

        retrun "".join(nums)