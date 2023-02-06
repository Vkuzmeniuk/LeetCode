class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            i += 1
        return i


sol = Solution()
print(sol.numberOfSteps(14))
