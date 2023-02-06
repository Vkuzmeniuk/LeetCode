
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True
        hashmap = {}
        print(f'ransomNote: {ransomNote}; magazine: {magazine};')
        for letter in set(ransomNote):
            hashmap[letter] = ransomNote.count(letter)
        for letter in hashmap:
            if (letter in hashmap) and (
                    hashmap[letter] <= magazine.count(letter)):
                result = True
            else:
                result = False
                break
        return result


sol = Solution()

ransomNote = "a"
magazine = "b"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "ihgg"
magazine = "ch"
print(sol.canConstruct(ransomNote, magazine))
