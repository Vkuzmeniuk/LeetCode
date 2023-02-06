from math import factorial,fabs
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        nlst = list(s1)
        # print(nlst)
        for i in range(1,factorial(len1)//len1 + 1):
            print(f'Factorial(len)//len1 = {factorial(len1)//len1}, iteration: {i}')
            for j in range(1,len1+1):
                k=j
                if k == len1:
                    k=1
                else:
                    k+=1
                # print(f'-j = {-j}, -k = {-k}')
                nlst[-j],nlst[-k]=nlst[-k],nlst[-j]
                print(nlst)
                if s2.find(''.join(nlst))>=0:
                    print('True')
                else:
                    continue

        return False
    
    
sol = Solution()

# s1 = "ab"
# s2 = "eidbaooo"
# print(f"Output: {sol.checkInclusion(s1, s2)}")

# s1 = "a"
# s2 = "ab"
# print(f"Output: {sol.checkInclusion(s1, s2)}")

s1 = "abcd"
s2 = "acbd"
print(f"Output: {sol.checkInclusion(s1, s2)}")