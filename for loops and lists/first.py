""""
# 1
def reverse_numbers(nums):
    nums = str(nums)
    nums = nums.split()
    return " ".join(nums[::-1])


print(reverse_numbers("3 6 9 12 15 18 21 24 27 30"))


# 2
def is_palindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return 1
    else:
        return 0


print(is_palindrome("ahmet"))


# 3
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

#5

def abs_diff():
    lst=[]
    input1=int(input("enter first"))
    for i in range(input1):
        lst.append(int(input("others")))

    x=[abs(lst[a]-lst[a+1]) for a in range(len(lst)-1)]
    return sum(x)
print(abs_diff())


#6
def largest_increment():
    input1=int(input("enter first number"))
    lst=[]
    for i in range(input1):
        lst.append(int(input("others")))

    x = [(lst[a+1] - lst[a]) for a in range(len(lst) - 1)]
    return max(x)
print(largest_increment())


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


#8
def find_most_repating(lst):
    set_lst={a: lst.count(a) for a in lst}
    max_count= max(set_lst.values())
    max_repeating_key=  {a:b for b,a in set_lst.items()}.get(max_count)
    return max_repeating_key, max_count
print(find_most_repating("А22Сс#AAAA4fffF"))

#9
def find_conjunction(set1,set2):
    conjunction=""
    for i in set1:
        for x in set2:
            if i==x and i not in conjunction:
                conjunction+= str(i)
    return conjunction
print(find_conjunction("abcde1234", "cdefg6789"))



#10
def find_difference(set1,set2):
    conjunction=""
    for i in set1:
        for x in set2:
            if i==x and i not in conjunction:
                conjunction+= str(i)
    diff=""
    for i in set1:
        if i not in conjunction:
            diff+= str(i)
    return diff

print(find_difference("abcde1234", "cdefg6789"))



#11

def find_union(set1,set2):
    conjunction=""
    for i in set1:
        if i not in conjunction:
            conjunction += str(i)
    for x in set2:
        if x not in conjunction:
            conjunction += str(x)
    return conjunction
print(find_union("abcde1234", "cdefg6789"))

"""
#12
def circle_table(first_number,second_number):
    x=second_number
    lst=list(range(1,first_number+1))
    lst2=[]
    for i in range(first_number):
        lst2.append(lst.pop((second_number%first_number)-1)
        x+= second_number
    return  lst2
print(5,2)