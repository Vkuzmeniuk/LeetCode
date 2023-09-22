from typing import List
class Solution:
    def all_averages(self, L):
        allA = []
        def extract(L):
            ixvar = [L[0],L[-1]]
            for i in ixvar:
                L.remove(i)
            allA.append(sum(ixvar)/2)
            while L:
                extract(L)
        extract(L)
        return allA
        
    def distinctAverages(self, nums: List[int]) -> int:
        nList = list(nums)
        nList.sort()
        return len(set(self.all_averages(nList)))
    
        

        
        
sol1 = Solution()
nums = [4,1,4,0,3,5]
print(nums)
print(sol1.distinctAverages(nums))

sol2 = Solution()
nums = [1,100]
print(nums)
print(sol1.distinctAverages(nums))