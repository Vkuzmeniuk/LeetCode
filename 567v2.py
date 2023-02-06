from math import factorial
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        nlst = list(s1)
        def swap(slst):
            hsmp = list()
            if slst:
                len1 = len(slst)
                for i in range(1,factorial(len1)//len1 + 1):
                    for j in range(1,len1+1):
                        #switching tail
                        k=j
                        if k == len1:
                            k=1
                        else:
                            k+=1
                        #swap  
                        slst[-j],slst[-k]=slst[-k],slst[-j]
                        # print(slst)
                        hsmp.append(''.join(slst))
            return hsmp
            
        def rec(lst1):
            head=list()
            tail=list(s1)
            tmps=list(lst1)
            for i in tmps:
                
                head.append(i)
                tail.remove(i)
                tmps.remove(i)
                
                print(f'HEAD: {head}; TAIL: {tail}; List: {lst1}; TMP: {tmps}')
                tswap = swap(tail)
                # print(tswap)
                for i in tswap:
                    head2 = list(head)
                    tail2=list(s1)
                    print(list(''.join(head2)+i))
                    # for j in head:
                    #     tail2.remove(i)
                    #     rec(tail2)
                        
                    
                return rec(tmps)
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