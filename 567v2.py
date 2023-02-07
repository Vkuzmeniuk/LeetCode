from math import factorial
from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1lst = list(s1)
        for j in permutations(s1lst):
            if s2.find(''.join(j)) >= 0:
                print(''.join(j))
                return True
            
        return False
    
    
sol = Solution()

s1 = "ab"
s2 = "eidbaooo"
print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "a"
s2 = "ab"
print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "abcd"
s2 = "acbd"
print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "dinitrophenylhydrazine"
s2 = "acetylphenylhydrazine"
print(f"Output: {sol.checkInclusion(s1, s2)}")