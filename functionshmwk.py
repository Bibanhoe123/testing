def exercise1(n,s):
    lengthadded = len(n)
    s = (s-lengthadded-1)*" "
    n = s + n
    return n

#n = input("pls enter a word")
#s = int(input("pls enter a number in which you would align your text to the right"))
#print(exercise1(n,s))

def exercise3(s):
    if s == "0" or s == "1" or s == "2"or s == "3"or s == "4"or s == "5"or s == "6"or s == "7"or s == "8"or s == "9":
        return True
    else:
        return False
s = input("see if wat you enter is a int")
#print(exercise3(s))
def exercise4(x):
    if x % 4 == 0:
        return True
    else:
        return False
x = int(input("enter a year"))
print(exercise4(x))

