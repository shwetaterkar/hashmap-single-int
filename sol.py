from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c_n=Counter(nums)
        print(c_n)
        for tmp in c_n:
            if(c_n.get(tmp)==1):
                return tmp
        
        
