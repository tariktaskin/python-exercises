"""
Question 11:
You will be given the elements
 of A set with N elements and B set
  with M elements (2 <= N, M <= 100).
   Write the program that finds the
    elements of the A⋃B set. In the first
     line of the entry, the number N will
      be given, followed by the elements
       of the A set. In the second line,
        first the number M, then the elements
         of the set B will be given. When 
         printing the result on the output,
          you must print the elements in the
           order they appear in set A.
            Intersections are guaranteed
             not to be empty sets. Set elements
              will only consist of alphabet letters
               and numbers.
"""

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