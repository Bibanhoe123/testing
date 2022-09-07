import math
def ques1():
    width = 17
    height = 12.0
    delimeter = "."
    width/2
    print(type(width),width)
    width/2.0
    print(type(width),width)
    height/3
    print(type(height) ,height)
    1 + 2 * 5
    delimeter * 5
    print(delimeter)
def ques2():
    r= 5.0
    volume = math.pi*r**3.0
    print(volume)

#ques2()
#ques1()
def ques3():
    starttime=(6*60+52)*60
    easytime=(8*60+15)*2
    tempotime = (7*60+12)
    brektime=(starttime+easytime+tempotime)/(60*60)
    brekhourint= int(brektime)

    brekminute=(brektime-brekhourint)*60
    brekminuteint=int(brekminute)
    print(f'{brekhourint}:{brekminuteint}')
    #print(tempotime)
#ques3()
def exercise4():
    r=7.25/100/12
    p=111000
    payments=30*12
    mortgpaymentmonth=(r/1-(1+r)**-payments)*p*-1
    print(f'{mortgpaymentmonth:.2f}$')
exercise4()









