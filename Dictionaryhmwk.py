import random
# #fix later
# def exercise1(adict):
#     randomnums = []
#     counter = 0
#     countrandnums=[]
#     keys=range(9)
#     for i in range(1000):
#         randomnums.append(random.randint(0,9))
#     #print(x)
#     for key in adict:
#         counter+=1
#         countrandnums.append(randomnums.count(counter)/1000*100)
#     print(adict)
#     counter=0
#     for i in keys:
#         counter+=1
#         adict[i+1] = countrandnums[i]
#         print(f'num {counter} ,chosen {adict[i+1]:.1f}%  time')
#
#
# randdict = {}
# exercise1(randdict)
# #
#
def exercise2():
    day =8
    year =85
    monthtonum= {"JAN": 1, "FEB" :2,"MAR":3,"APR":4,"MAY": 5, "JUN" :6,"JUL":7,"AUG":8,"SEP": 9, "OCT" :10,"NOV":11,"DEC":12}
def exercise3():
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----",
        "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
        "9": "----.", ".": ".-.-.-", ",": "--..--", " ": " "}
    key = morse.keys()
    morse = morse.values()

    entermorse = input("provide morse")
    for key , morses in morse.items():
        if morse = entermorse
            print(key)


        # dictionary = {'george': 16, 'amber': 19}
        # search_age = input("Provide age")
        # for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        #     if age == search_age:
        #         print(name)

