from math import factorial
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        nlst = list(s1)
        result = False
        def swap(slst):
            hsmp = list()
            if slst:
                len1 = len(slst)
                for i in range(1,factorial(len1)//len1 + 1):
                    for j in range(1,len1 + 1):
                        #switching tail
                        k=j
                        if k == len1:
                            k=1
                        else:
                            k+=1
                        #swap  
                        slst[-j],slst[-k]=slst[-k],slst[-j]
                        hsmp.append(''.join(slst))
            return hsmp
        
        def rec(lst1):
            head=list()
            tail=list(lst1)
            tmps=list(tail)
            for i in tmps:
                # print(f'Head: {head}; Tail: {tail}; TMPS: {tmps}')
                tswap_tail = swap(tail)
                tswap_head = swap(head)
                
                for j in tswap_tail:
                    if tswap_head:
                        for k in tswap_head:
                            if s2.find(str(k+j)) >= 0:
                                print(f'Found: {k+j}')
                                return True
                    else:
                        if s2.find(str(j)) >= 0:
                                print(f'Found: {j}')
                                return True
                head.append(i)
                tail.remove(i)
                
            return False
        
        return rec(nlst)
    
    
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