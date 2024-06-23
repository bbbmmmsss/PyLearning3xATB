#✅ Palidrome of String

# i/p = naman , nitin, level
# o/p = true
#
# i/p = pramod
# o/p = false
#

def isPalindrome(s):
    return s == s[::-1]
s = input("Enter a string: ")

ans = isPalindrome(s)
if ans:
    print("True")
else:
    print("False")



