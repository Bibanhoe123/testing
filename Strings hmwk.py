#exercise 1
# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
# if c is a lower case it returns true or false
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
# it wouldnt work
# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag
# it would only do the first value
# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag
#wouldnt work because when reran it would always be false
# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#     return True
#would work
# def exercise2(a):
#     revword= ""
#     for i in range(len(a)-1,-1,-1):
#         revword += a[i]
#     return revword
#
# a = input("enter a word to see if iys a palindrome")
# if exercise2(a) == a:
#     print("yes it is a palindrome")
# else: print("nope")
def exercise3(a,b):
    l = []
    i=0
    phrase=""
    for i in a:
        d = (ord(i))
        c = d+b
        if c >= 122:
            c = c-122+97
        phrase += chr(c)
    return c


a = input("pls enter a word to rotate ")
b =  int(input("pls enter a nuber of the amount of times you would like to rotate it over a number"))
print(exercise3(a,b))