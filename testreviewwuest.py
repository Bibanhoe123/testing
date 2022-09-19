# Start with a small number, n , 1 <= n <= 30.
#
# There are two transformation rules that we will use:
#
# If n is odd, multiple by 3 and add 1 to create a new value for n .
# If n is even, divide by 2 to create a new value for n .
# Perform a loop with these two transformation rules until you get to n = 1. You'll note that when n = 1, you get a repeating sequence of 1, 4, 2, 1, 4, 2, ...
#
# You can test for oddness using the % (remainder) operation. If n % 2 == 1, the number is odd, otherwise it is even.
#
# The two interesting facts are the “path length”, the number of steps until you get to 1, and the maximum value found during the process.
#
# Tabulate the path lengths and maximum values for numbers 1..30. You'll need an outer loop that ranges from 1 to 30. You'll need an inner loop to perform the two steps for computing a new n until n == 1; this inner loop will also count the number of steps and accumulate the maximum value seen during the process.
#
# Check: for 27, the path length is 111, and the maximum value is 9232.
#
# Additional Contest Style Challenges
import random
def hailstorm(input):
    x = []
    while input > 1:
        x.append(int(input))
        if input % 2 == 1:
            input = int(input*3+1)
        else:
            input = int(input/2)
        x.append(1)
    return x
def even_odd_list(number_values, low_value, high_value):
    for i in range(5):
        x = random.randint(low,high)
        if x%2 == 0:
            list.append(x)
        else:
            x+=1
            list.append(x)
    for i in range(5):
        y=random.randint(low,high)
        if y %2 == 1:
            list.append(y)
        else:
            y+=1
            list.append(y)
    print(list)

list = []
low = 1
high = 50
input = 60
#even_odd_list(list,low,high)
# print(hailstorm(input))
def createschooldict(schoolcodes,schoolnames):
    dict = {}
    for i in range(len(schoolcodes)):
        key = schoolcodes[i]
        value = schoolnames[i]
        dict[key] = value
    return dict

codes = ["aph","irs","oak","ht","sta"]

highschool = ["abebey park","Irqouis","whiteoaks","Holy trinity","Saint thomas aquanis"]

print(createschooldict(codes,highschool))

