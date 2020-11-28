"""
Question 12:
N (<100) people sit around
 a round table. These persons
  are numbered from 1 to N in
   the clockwise direction.
    We remove the Kth (<= N)
     person from the table,
      starting with the 1st
       person and moving clockwise.
        Until the table is empty,
         write a program that finds
          the numbers of the people
           in the order in which they 
           leave the table. First N,
            then K number will be given.
"""
def circle_table(first_number,second_number):
    x=second_number
    lst=list(range(1,first_number+1))
    lst2=[]
    for i in range(first_number):
        lst2.append(lst.pop((second_number%first_number)-1)
        x+= second_number
    return  lst2
print(5,2)

"""not completed
!!!!
"""