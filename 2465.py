from typing import List
class Solution:
    def partition(self, L, lo, hi, idx):
        if lo == hi: return lo
        L[idx],L[lo] = L[lo],L[idx]
        i = lo
        j = hi + 1
        while True:
            while True:
                i += 1
                if i == hi: break
                if L[lo] < L[i]: break
            
            while True:
                j -= 1
                if j == lo: break
                if L[j] < L[lo]: break
            
            if i >= j: break
            L[i],L[j] = L[j],L[i]
        L[lo],L[j] = L[j],L[lo]
        return j
    
    def quick_sort(self, L):
        def qsort(lo, hi):
            if hi <= lo:
                return
            pivot_idx = lo
            location = self.partition(L, lo, hi, pivot_idx)
            qsort(lo,location-1)
            qsort(location+1,hi)
        qsort(0, len(L)-1)
    
    def all_averages(self, L):
        allA = []
        def delfromL(ixvar):
            for i in ixvar:
                L.remove(i)
            
        def minmax(L):
            mi = L[0]
            ma = L[-1]
            return [mi,ma]
        
        def average(L):
            ixvar = minmax(L)
            delfromL(ixvar)
            return sum(ixvar)/2

        def extract(L):
            allA.append(average(L))
            while L:
                extract(L)
                
        extract(L)
        return allA
        
    def distinctAverages(self, nums: List[int]) -> int:
        nList = list(nums)
        self.quick_sort(nList)
        return len(set(self.all_averages(nList)))
    
        

        
        
sol1 = Solution()
nums = [4,1,4,0,3,5]
print(nums)
print(sol1.distinctAverages(nums))

sol2 = Solution()
nums = [1,100]
print(nums)
print(sol1.distinctAverages(nums))