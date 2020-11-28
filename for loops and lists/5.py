#5
"""
Write the program that 
finds the sum of the absolute
 values of the differences between
  two consecutive elements in an 
  integer list with N (2 <N <100) elements.

"""

def abs_diff():
    lst=[]
    input1=int(input("enter first"))
    for i in range(input1):
        lst.append(int(input("others")))

    x=[abs(lst[a]-lst[a+1]) for a in range(len(lst)-1)]
    return sum(x)
print(abs_diff())
