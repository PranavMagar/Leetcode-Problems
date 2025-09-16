lass Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for i in digits:
            nums = nums * 10 + i
        return (list(map(int,str(nums))))
