def exercise1(n,s):
    lengthadded = len(n)* " "
    s = s*" "+ lengthadded
    n = n + lengthadded
    print(s+n)
    return(n,s)

n = input("pls enter a word")
s= int(input("pls enter a number in which you would align your text to the right"))
exercise1(n,s)

