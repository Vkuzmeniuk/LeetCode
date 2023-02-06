from math import factorial,fabs
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        nlst = list(s1)
        # hsmp = {}
        def swap(slst):
            len1 = len(slst)
            for i in range(1,factorial(len1)//len1 + 1):
                for j in range(1,len1+1):
                    k=j
                    if k == len1:
                        k=1
                    else:
                        k+=1
                    slst[-j],slst[-k]=slst[-k],slst[-j]
                    print(slst)
        def rec(lst1): 
            result=list(s1)
            mps=list(lst1)
            for i in sorted(mps):
                # result.remove(i)
                mps.remove(i)
                for j in mps:
                    result.remove(j)
                print(f'HEAD: {result}; TMPS: {mps}; List: {lst1}')
                swap(mps)
                # for k in range(0, len(mps)):
                #     tresult=list()
                #     tmps=list(mps)
                #     j=k
                #     if j+1 > len1:
                #         j=1
                #     else:
                #         j+=1
                #     tmps[-j],tmps[-k]=tmps[-k],tmps[-j]
                #     tmps = ''.join(tmps)
                #     tresult.append(tmps)
                #     tresult = ''.join(tresult)
                #     print(''.join(result)+tresult) #Отсюда можно сделать сравнение со второй строкой
                return rec(mps)
        rec(nlst)            
            

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