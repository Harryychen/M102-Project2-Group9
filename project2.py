import random;
def sig_sim():
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
    print(cafe_day);
    print(cafe_happiness);
    return cafe_happiness;
sig_sim();