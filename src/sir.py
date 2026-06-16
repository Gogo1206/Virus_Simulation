import matplotlib.pyplot as plt
import numpy as np

import variable


def Average(lst):
    """Return the arithmetic mean of a list."""
    return sum(lst) / len(lst)


def cal_infection_rate(people, hours):
    """Calculate and graph the infection rate for a given population."""
    average_infect = 0
    for p in people:
        average_infect += p.infected
    average_infect = average_infect / len(people)

    levels = []
    for p in people:
        if p.infection_level != -1:
            if len(levels) - 1 < p.infection_level:
                levels.append(1)
            else:
                levels[p.infection_level] += 1
    infection_rates = []
    for i in range(len(levels) - 1):
        infection_rates.append(levels[i + 1] / levels[i])
    infection_rate = Average(infection_rates)
    average_infection_rate = (average_infect + infection_rate) / 2
    print("The average infection rate of two method is ",
          average_infection_rate)
    SIR.graph_SIR(hours, average_infection_rate, 1 / 7.5)


class SIR:
    """SIR epidemic model for graphing susceptible-infected-recovered curves."""

    def __init__(self, days, infection_rate, recovery_rate,
                 starting_infected_proportion=0.005):
        self.DAYS_NUMBER = days
        self.dt = 1  # time step in days
        self.BETA = infection_rate
        self.GAMMA = recovery_rate

        self.S = [1]  # susceptible
        self.I = [starting_infected_proportion]  # infected
        self.R = [0]  # recovered
        self.time = np.arange((self.DAYS_NUMBER + 1) * 24) * self.dt

    def model(self):
        """Run the SIR model simulation."""
        for hour in range(self.DAYS_NUMBER * 24):
            self.S.append(self.S[hour] - (self.BETA / 24)
                          * (self.S[hour] * self.I[hour]) * self.dt)
            self.I.append(self.I[hour] + ((self.BETA / 24)
                          * self.S[hour] * self.I[hour]
                          - (self.GAMMA / 24) * self.I[hour]) * self.dt)
            self.R.append(self.R[hour] + ((self.GAMMA / 24)
                          * self.I[hour]) * self.dt)

    def plot(self):
        """Plot the SIR curves using matplotlib."""
        fig = plt.figure(1)
        fig.clf()

        plt.plot(self.S, 'b', lw=3, label='Susceptible')
        plt.plot(self.I, 'r', lw=3, label='Infected')
        plt.plot(self.R, 'g', lw=3, label='Recovered')
        fig.legend()
        plt.xlabel('Hours')
        plt.xlim([0, 24 * self.DAYS_NUMBER])
        plt.ylabel('Fraction of Population')
        plt.show()

    @staticmethod
    def graph_SIR(hours, infection_rate, recovery_rate):
        """Create, model, and plot an SIR graph for given parameters."""
        sir = SIR(int(hours / 24), infection_rate, recovery_rate)
        sir.model()

        peak = 0
        for i in sir.I:
            peak = max(i, peak)
        print("SIR peak infection: ", int(peak * variable.NUM_PEOPLE))

        sir.plot()
