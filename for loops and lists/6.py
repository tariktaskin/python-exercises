"""
Write the program that
 finds the largest positive
  increment in an integer
   list with N (2 <N <100) elements.
"""
#6
def largest_increment():
    input1=int(input("enter first number"))
    lst=[]
    for i in range(input1):
        lst.append(int(input("others")))

    x = [(lst[a+1] - lst[a]) for a in range(len(lst) - 1)]
    return max(x)
print(largest_increment())
