from collections import Counter
class Solution:
    def singleNumber(self,nums:List[int])->List[int]:
        stack = []
        stack2 = []
        count = Counter(nums)
        for i in count:
            if count[i]>1:
                stack.append(i)
            else:
                stack2.append(i)
        return stack2
