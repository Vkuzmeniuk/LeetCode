class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def rpl(a, b): return a.replace(b, "")
        
        tmp_wrd = ""
        for ltr in str2:
            tmp_wrd += ltr
            
            if (str1 == str2):
                tmp_wrd = str2
                break
            else:
                if (str1.find(tmp_wrd)) < 0:
                    tmp_wrd = ""
                    break
                elif (str2.find(tmp_wrd)) >= 0 and not rpl(str2, tmp_wrd) == "":
                    continue
                else:
                    tmp_wrd[: len(tmp_wrd)]
                    break
            
        if  ((str1.count(tmp_wrd) % str2.count(tmp_wrd)) == 0) and (str2.count(tmp_wrd) > 1):
            tmp_wrd *= int(str1.count(tmp_wrd) / str2.count(tmp_wrd))

        if not rpl(str1, tmp_wrd) == "":
            tmp_wrd = ""
        
        return tmp_wrd


sol = Solution()

str1 = "ABCABC"
str2 = "ABC"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: ABC")


str1 = "ABABAB"
str2 = "ABAB"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: AB")

str1 = "LEET"
str2 = "CODE"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: ")

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: TAUXX")

str1 = "ABCDEF"
str2 = "ABC"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: ")

str1 = "ABABABAB"
str2 = "ABAB"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: ABAB")

str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: The fucking same")