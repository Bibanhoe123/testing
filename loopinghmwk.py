def question2():
    n = int(input("enter a number to see its closest power of 2 that is not higher then it"))
    p=1
    done=0
    count=0
    while n>=done:
        count+=1
        done = 2 * 2 * p
        p *= 2
    print(f'{2}^{count}')

#question2()
def question3():
    a="  "
    t=40
    v=5
    count=0
    for i in range(0,14,):
        for i in range(0,8):
            count+=1
            w = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
            v+=5
            print(f'{a}{w:>.0f}')
        t -= 5
        a*=2





    #for i in range

question3()