class Solution:
    def removeDuplicate(self,nums: List[int])->int:
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j += 1
        print(nums)
