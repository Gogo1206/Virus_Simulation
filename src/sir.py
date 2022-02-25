import excel
import matplotlib.pyplot as plt
import numpy as np


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
    print(infection_rate)
    average_infection_rate = (average_infect+infection_rate)/2
    print("The average infection rate of two method is ",average_infection_rate)
    graph_SIR(hours, average_infection_rate, 1/7.5)


class SIR():
    '''graph the SIR model'''
    def __init__(self, days = 100, infection_rate = (1/3), recovery_rate = (1/ 10), starting_infected_porportion = 0.001):
        self.DAYS_NUMBER = days
        self.dt = 1 # time steps in day
        self.BETA = infection_rate
        self.GAMMA = recovery_rate

        self.S = np.zeros((self.DAYS_NUMBER + 1) * 24) # susceptible
        self.I = np.zeros((self.DAYS_NUMBER + 1) * 24) # infected
        self.R = np.zeros((self.DAYS_NUMBER + 1) * 24) # recovered
        self.time = np.arange((self.DAYS_NUMBER + 1) * 24) * self.dt

        #proportion
        self.I[0] = starting_infected_porportion #initial infected
        self.S[0] = 1 - self.I[0] #initial susceptible
        self.R[0] = 0 #initial recovered

    def model(self):
        for hour in range(self.DAYS_NUMBER * 24):
            self.S[hour + 1] = self.S[hour] - (self.BETA / 24) * (self.S[hour] * self.I[hour]) * self.dt
            self.I[hour + 1] = self.I[hour] + ((self.BETA / 24) * self.S[hour] * self.I[hour] - (self.GAMMA / 24) * self.I[hour]) * self.dt
            self.R[hour + 1] = self.R[hour] + ((self.GAMMA / 24) * self.I[hour]) * self.dt

    def plot(self):
        fig = plt.figure(1) 
        fig.clf()
    
        plt.plot(self.time, self.S, 'b', lw=3, label = 'Susceptible')
        plt.plot(self.time, self.I, 'r', lw=3, label = 'Infected')
        plt.plot(self.time, self.R, 'g', lw=3, label = 'Recovered')
        fig.legend()
        plt.xlabel('Hours')
        plt.xlim([0, 24 * (self.DAYS_NUMBER)])
        plt.ylabel('Fraction of Population')
        plt.show()

def graph_SIR(hours,infection_rate,recovery_rate):
    sir = SIR(int(hours/24), infection_rate,recovery_rate)
    sir.model()
    sir.plot()
    
    max = 0
    for i in sir.I:
        if(i > max):
            max = i
    print("SIR peak infection: ",max)