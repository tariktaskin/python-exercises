"""In a 15-element
 list, find the maximum 
 consecutively repeating 
 character, and print the
  number of repetition.
"""
def find_most_repating(lst):
    set_lst={a: lst.count(a) for a in lst}
    max_count= max(set_lst.values())
    max_repeating_key=  {a:b for b,a in set_lst.items()}.get(max_count)
    return max_repeating_key, max_count
print(find_most_repating("А22Сс#AAAA4fffF"))