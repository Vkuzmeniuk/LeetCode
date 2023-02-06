class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            print(f'len1 % {k} = {len1 % k}({bool(len1 % k)}) or len2 % {k} = {len2 % k}({bool(len2 % k)})')
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            print(f'base = {base}')
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            print(f'len1={len1}; len2={len2};i={i}')
            if valid(i):
                return str1[:i]
        return ""

sol = Solution()

str1 = "ABCABC"
str2 = "ABC"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: ABC")


str1 = "ABABAB"
str2 = "ABAB"
print(f"Output: {sol.gcdOfStrings(str1, str2)}")
print("Expected: AB")

# str1 = "LEET"
# str2 = "CODE"
# print(f"Output: {sol.gcdOfStrings(str1, str2)}")
# print("Expected: ")

# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# print(f"Output: {sol.gcdOfStrings(str1, str2)}")
# print("Expected: TAUXX")

# str1 = "ABCDEF"
# str2 = "ABC"
# print(f"Output: {sol.gcdOfStrings(str1, str2)}")
# print("Expected: ")

# str1 = "ABABABAB"
# str2 = "ABAB"
# print(f"Output: {sol.gcdOfStrings(str1, str2)}")
# print("Expected: ABAB")

# str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
# str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
# print(f"Output: {sol.gcdOfStrings(str1, str2)}")
# print("Expected: The fucking same")