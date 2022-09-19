import random
# def exercise1(alist):
#     i = 1 #think this is the key so no index out of bounds
#     flag = False
#     while i < len(alist):
#         if alist[i] < alist[i-1]:
#             flag = True
#         i+=1
#     if flag == True:
#         print("moms spghetti")
#     else:
#         print("speghetti")
#
#
#
# numlist = [1,1,2,8]
# print(exercise1(numlist))


def exercise2(thelist):
    i = 0
    b = 0

    for i in range(len(thelist)-1):#list is 6
        b+=1
        if thelist[i] == thelist[b]:
            return True
        elif b == (len(thelist)-1):
            i+=1
    return False
thelist= [4,2,8,3,4,7]
print(exercise2(thelist))
def exercise3():
    for i in range(0,100):
        randomlist = []
        x = random.random()
        randomlist.append(x)
        print(randomlist)
# exercise3()

#
# def exercise2(thelist):
#     i = 0
#     b = 0
#     for i in range(len(thelist[:-1])):
#         b+=1
#         if thelist[i] == thelist[b]:
#             return True
#         elif b == (len(thelist[:-1])):
#             i+=1
#         else:
#             return False
# thelist=[1,2,1,4,5,"a",6,"a"]
# thelist.sort()
# print(exercise2(thelist))

