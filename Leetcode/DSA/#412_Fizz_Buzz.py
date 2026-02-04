# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/


def fizzBuzz(n: int):
        return [ 
            "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
            for i in range(1, n + 1)
            ]