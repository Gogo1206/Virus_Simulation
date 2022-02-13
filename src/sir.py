import excel
import person

def Average(lst):
    return sum(lst) / len(lst)

def cal_sir(S, I, R):
    infection_rates = []
    recovery_rates = []
    for i in range(0,len(S)-1):
        infection_rate = (S[i]-S[i+1])/I[i]
        # excel.write(i+1,4,infection_rate)
        recovery_rate = (R[i+1]-R[i])/I[i]
        # excel.write(i+1,5,recovery_rate)
        if(infection_rate != 0):
            infection_rates.append(infection_rate)
        if(recovery_rate != 0):
            recovery_rates.append(recovery_rate)
        # print("infection rate is in hour ",i," is: ",infection_rates[i],"recovery rate is in hour ",i," is: ",recovery_rates[i])
    avg_infection_rate = Average(infection_rates)
    avg_recovery_rate = Average(recovery_rates)
    print("Average infection rate is: ",avg_infection_rate,", Average recovery rate is: ",avg_recovery_rate)
    
def cal_infection_rate(people):
    average_infect = 0
    for p in people:
        average_infect+=p.infected
    average_infect=average_infect/len(people)
    print(average_infect)

    levels = []
    for p in people:
        if(p.infection_level != -1):
            if(len(levels) - 1 < p.infection_level):
                levels.append(1)
            else:
                levels[p.infection_level] += 1
    for i in range(len(levels)):
        print("Level ",i," has ",levels[i])
    infection_rates = []
    for i in range(len(levels)-1):
        infection_rates.append(levels[i+1]/levels[i])
    infection_rate = Average(infection_rates)
    print(Average(infection_rates))
    print("The average infection rate of two method is ",(average_infect+infection_rate)/2)
    