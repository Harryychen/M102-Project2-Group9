#ECS 101-M102-Project2-Group9
#Johnny Bai

#run the code in Python Console
#type-import simulation
#type-simulation.Simulation(t)
#t is the number of times you want to run
#the value and statement will print out

def exploitOnly():
    import random
    #Input values
    H1 = 9
    D1 = 3
    H2 = 7
    D2 = 5
    H3 = 11
    D3 = 7

    #make first random value of c1,c2,c3
    c1Happy = random.normalvariate(H1, D1)  #Happyvalue of Cafe1
    c2Happy = random.normalvariate(H2, D2)  #Happyvalue of Cafe2
    c3Happy = random.normalvariate(H3, D3)  #Happyvalue of Cafe3

    firstlist = [c1Happy, c2Happy, c3Happy] #First time to eat
    firstsum = firstlist[0] + firstlist[1] + firstlist[2]
    maxfirst = max(firstlist)                 #find the best one in the third day
    indexlist = firstlist.index(maxfirst) + 1

    resthappy = 0                           #find the rest 297 day of happy
    if indexlist == 1:
        for i in range(297):
            c1Happy = random.normalvariate(H1, D1)  # Happyvalue of Cafe1
            resthappy = resthappy + c1Happy
    elif indexlist == 2:
        for i in range(297):
            c2Happy = random.normalvariate(H2, D2)  #Happyvalue of Cafe2
            resthappy = resthappy + c2Happy
    else:
        for i in range(297):
            c3Happy = random.normalvariate(H3, D3)  #Happyvalue of Cafe3
            resthappy = resthappy + c3Happy

    totalhappy = firstsum + resthappy

    exphappy = H1 + H2 + H3 + H3*297

    regret = exphappy - totalhappy

    return totalhappy

    #print statement
    print("happiness exploitonly", totalhappy)
    print("regret exploitonly", regret)

def exploreOnly():
    import random
    # Input values
    H1 = 9
    D1 = 3
    H2 = 7
    D2 = 5
    H3 = 11
    D3 = 7

    c1Happyall = 0  #toal happy of cafe 1
    for i in range(100):
        c1Happy = random.normalvariate(H1, D1)  # Happyvalue of Cafe1
        c1Happyall = c1Happyall + c1Happy

    c2Happyall = 0  #total happy of cafe 2
    for i in range(100):
        c2Happy = random.normalvariate(H2, D2)# Happyvalue of Cafe2
        c2Happyall = c2Happyall + c2Happy

    c3Happyall = 0
    for i in range(100):
        c3Happy = random.normalvariate(H3, D3)  # Happyvalue of Cafe3
        c3Happyall = c3Happyall +c3Happy

    totalhappy = c1Happyall + c2Happyall +c3Happyall

    exphappy = 100*H1 + 100*H2 + 100*H3

    regret = exphappy - totalhappy

    return totalhappy

    #print statement
    print("happiness exploitonly", totalhappy)
    print("regret exploitonly", regret)

def eGreddy():
    import random
    #Input values
    H1 = 9
    D1 = 3
    H2 = 7
    D2 = 5
    H3 = 11
    D3 = 7

    e = 12/100  #the e value in decimal

    #Sum, Number and average of Cafe1
    sumc1Happy = 0
    numc1 = 0
    avec1Happy = 0

    #Sum, Number and average of Cafe2
    sumc2Happy = 0
    numc2 = 0
    avec2Happy = 0

    #Sum, Number and average of Cafe3
    sumc3Happy = 0
    numc3 = 0
    avec3Happy = 0
    for i in range(300):
        r = random.random()     #make a random numble
        if r < e:   #pick a random Cafe
            cafenum = random.randint(1, 3)
            if cafenum == 1:
                c1Happy = random.normalvariate(H1, D1)
                sumc1Happy = sumc1Happy + c1Happy   #total happy of Cafe1
                numc1 = numc1 + 1                   #number of times eat in Cafe1
                avec1Happy = sumc1Happy/numc1       #average value of Cafe1 happy
            if cafenum == 2:
                c2Happy = random.normalvariate(H2, D2)
                sumc2Happy = sumc2Happy + c2Happy   # total happy of Cafe2
                numc2 = numc2 + 1                   # number of times eat in Cafe2
                avec2Happy = sumc2Happy / numc2     # average value of Cafe2 happy
            else:
                c3Happy = random.normalvariate(H3, D3)
                sumc3Happy = sumc3Happy + c3Happy   # total happy of Cafe3
                numc3 = numc3 + 1                   # number of times eat in Cafe3
                avec3Happy = sumc3Happy / numc3     # average value of Cafe3 happy
        else:   #pick the one is best untile now
            numlist = [avec1Happy, avec2Happy, avec3Happy]
            maxnum = max(numlist)
            cafenum = numlist.index(maxnum) + 1
            if cafenum == 1:
                c1Happy = random.normalvariate(H1, D1)
                sumc1Happy = sumc1Happy + c1Happy   #total happy of Cafe1
                numc1 = numc1 + 1                   #number of times eat in Cafe1
                avec1Happy = sumc1Happy/numc1       #average value of Cafe1 happy
            if cafenum == 2:
                c2Happy = random.normalvariate(H2, D2)
                sumc2Happy = sumc2Happy + c2Happy   # total happy of Cafe2
                numc2 = numc2 + 1                   # number of times eat in Cafe2
                avec2Happy = sumc2Happy / numc2     # average value of Cafe2 happy
            else:
                c3Happy = random.normalvariate(H3, D3)
                sumc3Happy = sumc3Happy + c3Happy   # total happy of Cafe3
                numc3 = numc3 + 1                   # number of times eat in Cafe3
                avec3Happy = sumc3Happy / numc3     # average value of Cafe3 happy

    totalhappy = sumc1Happy + sumc2Happy + sumc3Happy

    exphappy = 0.88*300*11 + 0.04*300*9 + 0.04*300*7 + 0.04*300*11

    regret = exphappy - totalhappy

    return totalhappy

    #print statement
    print("happiness eGreddy", totalhappy)
    print("regret eGreddy", regret)

def Simulation(t):
    #exploit Only function
    sumHappyPloit = 0
    sumRegretPloit = 0
    exphappyPloit = 9 + 7 + 11 + 11 * 297
    for i in range(t):
        happyPloit = exploitOnly()
        regretPloit = exphappyPloit - happyPloit
        sumHappyPloit = sumHappyPloit + happyPloit
        sumRegretPloit = sumRegretPloit + regretPloit
    aveHappyPloit = sumHappyPloit/t
    aveRegretPloit = sumRegretPloit/t
    print("Ave happiness exploitonly", aveHappyPloit)
    print("Ave regret exploitonly", aveRegretPloit)

    #explore Only function
    sumHappyPlore = 0
    sumRegretPlore = 0
    exphappyplore = 100 * 9 + 100 * 7 + 100 * 11
    for i in range(t):
        happyPlore = exploreOnly()
        regretPlore = exphappyplore - happyPlore
        sumHappyPlore = sumHappyPlore + happyPlore
        sumRegretPlore = sumRegretPlore + regretPlore
    aveHappyPlore = sumHappyPlore/t
    aveRegretPlore = sumRegretPlore/t
    print("Ave happiness exploreonly", aveHappyPlore)
    print("Ave regret exploreonly", aveRegretPlore)

    #e Greddy function
    sumHappyGreddy = 0
    sumRegretGreddy = 0
    expGreddy = 0.88*300*11 + 0.04*300*9 + 0.04*300*7 + 0.04*300*11
    for i in range(t):
        happyGreddy = eGreddy()
        regretGreddy = expGreddy - happyGreddy
        sumHappyGreddy = sumHappyGreddy + happyGreddy
        sumRegretGreddy = sumRegretGreddy + regretGreddy
    aveHappyGreddy = sumHappyGreddy/t
    aveRegretGreddy = sumRegretGreddy/t
    print("Ave happiness greddy", aveHappyGreddy)
    print("Ave regret greddy", aveRegretGreddy)