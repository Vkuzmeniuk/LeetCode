
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        common_letters = set(ransomNote) & set(magazine)
        result = True
        print(
            f'ransomNote: {ransomNote}; magazine: {magazine}; intersect: {common_letters}')
        if common_letters:
            # for letter in common_letters:
            #     print(f'letter: {letter}; magazine count: {magazine.count(letter)}; ransomNote count: {ransomNote.count(letter)}')
            #     if magazine.count(letter) < ransomNote.count(letter):
            #         result = False
            for letter in ransomNote:
                if magazine.count(letter) < ransomNote.count(letter):
                    result = False

        else:
            result = False
        return result


sol = Solution()
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "ihgg"
magazine = "ch"
print(sol.canConstruct(ransomNote, magazine))

ransomNote = "ihgg"
magazine = "ch"
