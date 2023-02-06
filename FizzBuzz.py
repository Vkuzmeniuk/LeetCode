class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        c = []
        for x in list(range(1, n + 1)):
            if x % 3 == 0 and x % 5 == 0:
                c.append('FizzBuzz')
            elif x % 5 == 0:
                c.append('Buzz')
            elif x % 3 == 0:
                c.append('Fizz')
            else:
                c.append(x)
        return c


sol = Solution()
print(sol.fizzBuzz(100))
