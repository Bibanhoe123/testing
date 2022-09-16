import random

#fix later
def exercise1(adict):
    numbers = {}
    randomnums = []
    counter = 0
    for i in range(11):
        numbers[i] = 0
    for i in range(1000):
        randomnums.append(random.randint(0,10))
    for i in randomnums:#goes tthrough random list lets say lands on 7(the key) numbers[7] allows += 1 to value<--adds a count for
        numbers[i] += 1#<---count
    print(numbers)
    #print(x)
    #
    # for i in keys:
    #     counter+=1
    #     adict[i+1] = countrandnums[i]
    #     print(f'num {counter} ,chosen {adict[i+1]:.1f}%  time')


randdict = {}
#exercise1(randdict)
def exercise2(dict):
    date = ""
def exercise3():
    counter = 0
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

    newmorse = {}
    entermorse = (".... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   ... .- -   --- -.   .-   .-- .- .-.. .-.. .-.-.- .... ..- -- .--. - -.--   -.. ..- -- .--. - -.--   .... .- -..   .-   --. .-. . .- -   ..-. .- .-.. .-.. .-.-.- .- .-.. .-..   - .... .   -.- .. -. --. ...   .... --- .-. ... . ...   .- -. -..   .- .-.. .-..   - .... .   -.- .. -. --. ...   -- . -. .-.-.- -.-. --- ..- .-.. -.. -. -   .--. ..- -   .... ..- -- .--. - -.--   - --- --. . - .... . .-.   .- --. .- .. -. .-.-.- ")
    listenter = entermorse.split()
    print(listenter)
    for key in morse:
        newmorse[morse[key]] = key#<---key and [morse[key]] is value added
    print(newmorse)
    for i in listenter:# do for loop in listenter because goes through that list of strings
        pass#print(newmorse[i],end =" " )

#exercise3()
# def exercise4():
#     products = {}
#     prices = [3.98, 0.97, 2.97, 3.99, 3.98, 1.98, 3.98, 1.98, 1.98, 3.98, 2.98, 2.99, 3.97, 0.97, 1.99, 0.98, 0.97, 3.99, 2.99, 3.97, 3.99, 0.98, 3.97, 1.98, 2.99, 1.97, 2.98, 1.97, 0.98, 2.97, 3.97, 0.99, 1.97, 2.97, 2.99, 1.98, 0.98, 1.98, 1.97, 1.98, 2.99, 1.97, 0.98, 0.97, 1.99, 3.97, 2.99, 0.99, 3.98, 3.97, 3.97, 1.99, 3.97, 3.98, 1.98, 2.99, 2.97, 3.97, 3.99, 3.98, 3.99, 2.97, 0.97, 0.99, 1.97, 0.97, 2.99, 3.99, 0.99, 2.97, 0.98, 3.97, 1.99, 0.99, 1.97, 0.97, 0.97, 2.99, 0.99, 0.97, 3.97, 1.99, 2.98, 3.97, 3.99]
#     stuff = ['advil', 'aspirin', 'antacids', 'antibiotic ointment', 'anti-bacerial toweletters', 'automotive repair kits','baking tin', 'bandages', 'bandannas', 'baking soda', 'lighters', 'boxed food', 'bungee cords', 'cable ties','camping fuel', 'candles', 'canned fruits', 'canned meat', 'canned veggies', 'can openers', 'car towels', 'chewing gum', 'clothesline', 'coffee filters', 'combs', 'compact mirror', 'condiments', 'cotton balls', 'cokkie tins', 'cough drops', 'cutting boards', 'dental floss', 'digital thermometer', 'dish towels', 'dog food', 'duct tape', 'drop cloth', 'ear plugs', 'elastic hair bands', 'emergency cell phone chargers', 'epsom salts', 'eyeglass repair kit', 'facial tissues', 'gauze', 'gardening globes', 'hard candies', 'hydrogen peroxide', 'hand sanitizer', 'jarred foods', 'instant ice packs', 'knives', 'latex dishwashing gloves', 'lip balms', 'lotions', 'magnifying glass', 'matches', 'mesh laundry bag', 'nails', 'screws', 'plastic shoe container','rubbing alcohol', 'safety pins', 'salt with iodine', 'scrub buddies', 'sewing kit', 'shoe laces', 'soaps', 'socks', 'solar lights', 'spices', 'stell wool', 'sponges', 'sugar', 'super glue', 'sun hat', 'toothbrushes', 'tote bags', 'travel bottles', 'twine', 'utility pail', 'water', 'wet wipes']
#     for i in range (len(prices)):
#         if i >= len(stuff):
#
#
#         prices[i] = 0
#     print(products)
# #exercise4()



    #
    #
    #     sample_dict = {}
    #     keys = ['John', 'Mark', 'Aadi']
    #     values = [100, 200, 300]
    #     sample_dict = {key: value
    #                    for key, value in zip(keys, values)}
    #     print(sample_dict)
        #print(products)

    # for i in range len(prices):
    #     pass#print(products)
    # for i in prices:
    #     pass

def exercise5():
    d = {}
    d1= 0
    d2 = 0
    for i in range (7):
        d1 = i

        for j in range(7):
            d2 = j
            tuple = (i,j)
    for i in range(13):
        d[i] = 0
    #print(d)
        for i in d:
            d[i] = tuple
        print(d)

exercise5()
#     d = {}
#     Loop
#     with d1 from 1 to 6
#     Loop
#     with d2 from 1 to 6
#     new_tuple ← (d1, d2)  # create the tuple
#     sum ← d1 + d2
#     d[sum] = new_tuple
#
#
# Loop
# over
# all
# values in the
# dictionary
# print
# the
# key and the
# length
# of
# the
# list




    #print(products)
#exercise4()










# def reverse_dictionary(some_dict):
#     #create a dictionary in reverse
#     reverse_dict = {}
#
#     for key in some_dict.keys(): #interate over existing dictinary
#         reverse_dict[some_dict[key]] = key #adding new key/value pair
#
#     return reverse_dict




        # dictionary = {'george': 16, 'amber': 19}
        # search_age = input("Provide age")
        # for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        #     if age == search_age:


        # dictionary = {'george': 16, 'amber': 19}
        # search_age = input("Provide age")
        # for name, age in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        #     if age == search_age:
        #         print(name)


# dicts = {}
# keys = range(4)
# values = ["Hi", "I", "am", "John"]
# for i in keys:
#         dicts[i] = values[i]
# print(dicts)


