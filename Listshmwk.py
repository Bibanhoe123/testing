# def exercise1(alist):
#     i=0
#     b=0
#     for i in range (len(list[:-1])):
#         b += list[i]
#         a = list[i+1]
#         a-=1
#         if a == b:
#             return True
#     return False
#
#
# numlist = [0,2,3,3]
# print(exercise1(numlist))

def exercise2(thelist):
    i = 0
    b = 0
    for i in range (len(thelist[:-1])):
        b+=1
        if thelist[i]== thelist[b]:
            return True
        elif b == (len(thelist[:-1])):
            i+=1
        else:
            return False
    thelist(0,0,0,0,0,0)
