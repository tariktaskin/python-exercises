"""
In this problem you are given 
an even N (1 <N <100) number. 
Then N integers are given. Write 
a program that prints these given 
numbers such as one from beginning
 one from end and so on.

"""
#4
def front_back():
    x = int(input("enter first"))
    lst = []
    for i in range(x):
        lst.append(int(input("enter other numbers")))
    front = 0
    back = x
    lst2 = []
    for i in lst:
        if front >= back:
            break
        else:
            lst2.append(lst[front])
            lst2.append(lst[back - 1])
            front += 1
        back -= 1

    return lst2


print(front_back())