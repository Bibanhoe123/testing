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
exercise1(randdict)
def exercise2(dict):
    date = ""
def exercise3():
    counter = 0
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
def exercise4():
    keys = [3.98, 0.97, 2.97, 3.99, 3.98, 1.98, 3.98, 1.98, 1.98, 3.98, 2.98, 2.99, 3.97, 0.97, 1.99, 0.98, 0.97, 3.99, 2.99, 3.97, 3.99, 0.98, 3.97, 1.98, 2.99, 1.97, 2.98, 1.97, 0.98, 2.97, 3.97, 0.99, 1.97, 2.97, 2.99, 1.98, 0.98, 1.98, 1.97, 1.98, 2.99, 1.97, 0.98, 0.97, 1.99, 3.97, 2.99, 0.99, 3.98, 3.97, 3.97, 1.99, 3.97, 3.98, 1.98, 2.99, 2.97, 3.97, 3.99, 3.98, 3.99, 2.97, 0.97, 0.99, 1.97, 0.97, 2.99, 3.99, 0.99, 2.97, 0.98, 3.97, 1.99, 0.99, 1.97, 0.97, 0.97, 2.99, 0.99, 0.97, 3.97, 1.99, 2.98, 3.97, 3.99]
    values = ['advil', 'aspirin', 'antacids', 'antibiotic ointment', 'anti-bacerial toweletters', 'automotive repair kits','baking tin', 'bandages', 'bandannas', 'baking soda', 'lighters', 'boxed food', 'bungee cords', 'cable ties','camping fuel', 'candles', 'canned fruits', 'canned meat', 'canned veggies', 'can openers', 'car towels', 'chewing gum', 'clothesline', 'coffee filters', 'combs', 'compact mirror', 'condiments', 'cotton balls', 'cokkie tins', 'cough drops', 'cutting boards', 'dental floss', 'digital thermometer', 'dish towels', 'dog food', 'duct tape', 'drop cloth', 'ear plugs', 'elastic hair bands', 'emergency cell phone chargers', 'epsom salts', 'eyeglass repair kit', 'facial tissues', 'gauze', 'gardening globes', 'hard candies', 'hydrogen peroxide', 'hand sanitizer', 'jarred foods', 'instant ice packs', 'knives', 'latex dishwashing gloves', 'lip balms', 'lotions', 'magnifying glass', 'matches', 'mesh laundry bag', 'nails', 'screws', 'plastic shoe container','rubbing alcohol', 'safety pins', 'salt with iodine', 'scrub buddies', 'sewing kit', 'shoe laces', 'soaps', 'socks', 'solar lights', 'spices', 'stell wool', 'sponges', 'sugar', 'super glue', 'sun hat', 'toothbrushes', 'tote bags', 'travel bottles', 'twine', 'utility pail', 'water', 'wet wipes']
    products = dict(zip(keys, values))
    print(products)
    #
    # for key in prices:
    #     products[key] = 0 #ask her
    # print(products)
    #
    # for key, value in products:
    #     zip(prices,stuff)
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
    pass




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
        #         print(name)




# dicts = {}
# keys = range(4)
# values = ["Hi", "I", "am", "John"]
# for i in keys:
#         dicts[i] = values[i]
# print(dicts)

