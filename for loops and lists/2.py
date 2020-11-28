"""
Question 2:
Strings that read in reverse are the same as themselves are 
called palindromes. Find out if a string of 10
 elements given to you is a palindrome. If it is a palindrome, print 1 on the screen, otherwise 0.
"""
def is_palindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return 1
    else:
        return 0


print(is_palindrome("ahmet"))