from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, ln, match = Counter(s1), len(s1), 0
        print(cntr) 
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0: match += 1
            
            if i>=ln and s2[i-ln] in cntr:
                if cntr[s2[i-ln]] == 0: match -=1
                cntr[s2[i-ln]] +=1
        
            if match == len(cntr):
                return True
        print(cntr)
        
        return False
    
    
sol = Solution()

# s1 = "ab"
# s2 = "eidbaooo"
# print(f"Output: {sol.checkInclusion(s1, s2)}")

# s1 = "ba"
# s2 = "abc"
# print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "abcde"
s2 = "acbdsda"
print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"
print(f"Output: {sol.checkInclusion(s1, s2)}")