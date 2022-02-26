import excel
import matplotlib.pyplot as plt
import numpy as np
import variable


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
    
def cal_infection_rate(people,hours):
    '''calculate the infection rate for a given population'''
    average_infect = 0
    for p in people:
        average_infect+=p.infected
    average_infect=average_infect/len(people)
    # print(average_infect)

    levels = []
    for p in people:
        if(p.infection_level != -1):
            if(len(levels) - 1 < p.infection_level):
                levels.append(1)
            else:
                levels[p.infection_level] += 1
    # for i in range(len(levels)):
    #     print("Level ",i," has ",levels[i])
    infection_rates = []
    for i in range(len(levels)-1):
        infection_rates.append(levels[i+1]/levels[i])
    infection_rate = Average(infection_rates)
    # print(infection_rate)
    average_infection_rate = (average_infect+infection_rate)/2
    print("The average infection rate of two method is ",average_infection_rate)
    SIR.graph_SIR(hours,average_infection_rate,1/7.5)


class SIR():
    '''graph the SIR model'''
    def __init__(self, days, infection_rate, recovery_rate, starting_infected_porportion = 0.005):
        self.DAYS_NUMBER = days
        self.dt = 1 # time steps in day
        self.BETA = infection_rate
        self.GAMMA = recovery_rate

        self.S = [1] # susceptible
        self.I = [starting_infected_porportion] # infected
        self.R = [0] # recovered
        self.time = np.arange((self.DAYS_NUMBER + 1) * 24) * self.dt

    def model(self):
        for hour in range(self.DAYS_NUMBER * 24):
            self.S.append(self.S[hour] - (self.BETA / 24) * (self.S[hour] * self.I[hour]) * self.dt)
            self.I.append(self.I[hour] + ((self.BETA / 24) * self.S[hour] * self.I[hour] - (self.GAMMA / 24) * self.I[hour]) * self.dt)
            self.R.append(self.R[hour] + ((self.GAMMA / 24) * self.I[hour]) * self.dt)

    def plot(self):
        fig = plt.figure(1) 
        fig.clf()
    
        plt.plot(self.S, 'b', lw=3, label = 'Susceptible')
        plt.plot(self.I, 'r', lw=3, label = 'Infected')
        plt.plot(self.R, 'g', lw=3, label = 'Recovered')
        fig.legend()
        plt.xlabel('Hours')
        plt.xlim([0, 24 * (self.DAYS_NUMBER)])
        plt.ylabel('Fraction of Population')
        plt.show()
        
    def graph_SIR(hours,infection_rate,recovery_rate):
        sir = SIR(int(hours/24), infection_rate,recovery_rate)
        sir.model()
    
        peak = 0
        for i in sir.I:
            peak=max(i,peak)
        print("SIR peak infection: ",int(peak*variable.NUM_PEOPLE))
        
        sir.plot()