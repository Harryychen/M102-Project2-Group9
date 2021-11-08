def exploitOnly(H1:int, D1:int, H2:int, D2:int, H3:int, D3:int):
    import random
    c1Happy = random.normalvariate(H1, D1)  #Happyvalue of Cafe1
    c2Happy = random.normalvariate(H2, D2)  #Happyvalue of Cafe2
    c3Happy = random.normalvariate(H3, D3)  #Happyvalue of Cafe3
    numlist = [c1Happy, c2Happy, c3Happy]   #find the happiest Cafe amone three
    maxHappy = numlist[0]
    for item in numlist:
        if item > maxHappy:
            maxHappy = item
    totalHappy = maxHappy*297   #solved for the total Happiness

    mylist2 = [H1, H2, H3]      #sloved for the optimum Happiness
    maxaveHappy = mylist2[0]
    for item in mylist2:
        if item > maxaveHappy:
            maxaveHappy = item
    optimumHappy = maxaveHappy*300

    expectHappy = 100*H1 + 100*H2 + 100*H3      #sloved for the expected Happiness

    regretHappy = optimumHappy - totalHappy     #solved for the regret

    #print result:
    print(totalHappy)
    print(optimumHappy)
    print(expectHappy)
    print(regretHappy)
