#412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for val in range(1, n+1):
            if val % 15 == 0:
                res.append("FizzBuzz")
            elif val % 3 == 0:
                res.append("Fizz")
            elif val % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(val))
        return res
