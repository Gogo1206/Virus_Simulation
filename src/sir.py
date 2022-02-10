def Average(lst):
    return sum(lst) / len(lst)

def cal_sir(S, I, R):
    infection_rates = []
    recovery_rates = []
    for i in range(0,len(S)-1):
        infection_rate = (S[i]-S[i+1])/I[i]
        recovery_rate = (R[i+1]-R[i])/I[i]
        if(infection_rate != 0):
            infection_rates.append(infection_rate)
        if(recovery_rate != 0):
            recovery_rates.append(recovery_rate)
        # print("infection rate is in hour ",i," is: ",infection_rates[i],"recovery rate is in hour ",i," is: ",recovery_rates[i])
    avg_infection_rate = Average(infection_rates)
    avg_recovery_rate = Average(recovery_rates)
    print("Average infection rate is: ",avg_infection_rate,", Average recovery rate is: ",avg_recovery_rate)