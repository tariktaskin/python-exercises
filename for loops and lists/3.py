"""
In Fibonacci Numbers, each number progresses
 as the sum of the two preceding numbers, 
 such as 0,1,1,2,3,5,8, ... In this question
  you are given a number (0 <N <20). 
  Accordingly, write the program that prints 
  all Fibonacci numbers backwards from the Nth
   Fibonacci number. 

"""
def reverse_fib_series(num):
    x = []
    for i in range(num):
       if i == 0:
           x.append(0)
       elif i == 1:
           x.append(1)
       else:
           x.append(sum(reverse_fib_series(i)[-2:]))
   return x

reversed = reverse_fib_series(11)[::-1]
print(reversed)
