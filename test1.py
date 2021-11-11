import random;
def eGreedy(e):
    global cafe_day
    global cafe_happiness
    print("test")
    sig=0.2;
    total_day=300;
    day=0;
    cafe_day=[0,0,0];
    cafe_happiness=[0.0,0.0,0.0];
    cafe_hcoeff=[9,7,11];
    cafe_dcoeff=[3,5,7];
    for i in range(0,300):
        if(random.random()<sig):
            chosen_cafe=random.randint(1,3);
            day=day+1;
            cafe_day[chosen_cafe-1]=cafe_day[chosen_cafe-1]+1;
            cafe_happiness[chosen_cafe-1]=(cafe_happiness[chosen_cafe-1]*(cafe_day[chosen_cafe-1]-1)+random.normalvariate(cafe_hcoeff[chosen_cafe-1],cafe_dcoeff[chosen_cafe-1]))/cafe_day[chosen_cafe-1];
        else:
            chosen_cafe=0;
            max_happiness=cafe_happiness[0];
            for j in range(0,3):
                if cafe_happiness[j]>max_happiness:
                    max_happiness=cafe_happiness[j];
                    chosen_cafe=j;
            day=day+1;
            chosen_cafe=chosen_cafe+1;
            cafe_day[chosen_cafe-1]=cafe_day[chosen_cafe-1]+1;
            cafe_happiness[chosen_cafe-1]=(cafe_happiness[chosen_cafe-1]*(cafe_day[chosen_cafe-1]-1)+random.normalvariate(cafe_hcoeff[chosen_cafe-1],cafe_dcoeff[chosen_cafe-1]))/cafe_day[chosen_cafe-1];
    totalhappye = 0
    for i in range(len(cafe_day)):
        totalhappye += cafe_day[i] * cafe_happiness[i]
    print(totalhappye)
    print(cafe_day);
    print(cafe_happiness);

    return totalhappye;

def exploitOnly():
    global maxHappy
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

    return expectHappy
    #print result:
    print(totalHappy)
    print(optimumHappy)
    print(expectHappy)
    print(regretHappy)
    import random
def exploreOnly():
    totalHappiness = 0
    for i in ['c1', 'c2', 'c3']:
        if i == 'c1':
            mean = 9
            deviation = 3
        elif i == 'c2':
            mean = 7
            deviation = 5
        elif i == 'c3':
            mean = 11
            deviation = 7
        for j in range(1, 100):
            totalHappiness += random.normalvariate(mean, deviation)

    return totalHappiness
    print('total sum', totalHappiness)

    if __name__ == "__main__":
        exploreOnly()

def simulation(e, t):
    exploitcount = 0
    explorecount = 0
    greedycount = 0
    totalgreedyhappiness = 0
    totalexploithappiness = 0
    totalexplorehappiness = 0
    while greedycount < t:
        simu = eGreedy(e)
        totalgreedyhappiness += simu
        greedycount += 1
    while explorecount < t:
        simu = exploreOnly()
        totalexplorehappiness += simu
        explorecount += 1
    while exploitcount < t:
        simu = exploitOnly()
        totalexploithappiness += simu
        exploitcount += 1
        averagegreedy = totalgreedyhappiness / greedycount
        averageexplore = totalexplorehappiness / explorecount
        averageexploit = totalexploithappiness / exploitcount
        expectedHappy = 100 * 9 + 100 * 7 + 100 * 11
        expectedexploit = 9 + 7 + 11 + 297 *maxHappy
        expectedgreedy = 0
    for i in range(len(cafe_day)):
        expectedgreedy += cafe_day[i] * cafe_happiness[i]