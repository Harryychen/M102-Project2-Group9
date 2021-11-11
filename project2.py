def exploitOnly():
    import random
    #Input values
    H1 = 9
    D1 = 3
    H2 = 7
    D2 = 5
    H3 = 11
    D3 = 7
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
