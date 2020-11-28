
"""
Write the program that
 finds the length of the
  longest ascending consecutive
   sublist in an integer list 
   with N (2 <N <100) elements.
"""

#7
def longest_consecutive():
    input1=int(input("enter first number"))
    lst=[]
    for i in range(input1):
        lst.append(int(input("others")))

    count=0
    lst_counts=[]
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            count+=1
        else:
            lst_counts.append(count)
            count=0
    return  max(lst_counts) +1
print(longest_consecutive())
