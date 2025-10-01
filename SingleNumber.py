from collections import Counter
class Solution:
    def singleNumer(self,nums: List[int])->int:
        stack = []
        stack2 = []
        count = Counter(nums)
        for i in count:
            if count[i]>1:
                stack.append(i)
            else:
                stack2.append(i)
        for i in stack2:
            return i

