import random
from time import sleep
import variable
import person
import ui
import matplotlib.pyplot as plt
import time

start_time = time.time()

#saturated = false;

def try_event(probability):
	rnum = (int(random.uniform(0,100))+1)/100
	return rnum <= probability

def sim_main():
	vulnerable_history = [0] * variable.SIM_HOURS
	incubation_history = [0] * variable.SIM_HOURS
	asymptomatic_history = [0] * variable.SIM_HOURS
	symptomatic_history = [0] * variable.SIM_HOURS
	infected_history = [0] * variable.SIM_HOURS
	immune_history = [0] * variable.SIM_HOURS
	dead_history = [0] * variable.SIM_HOURS

	people = [person.Person()] * variable.NUM_PEOPLE
	for i in range (variable.NUM_PEOPLE):
		people[i] = person.Person()
		people[i].mask_check()
		people[i].vaccine_check()
  
	for i in range (variable.INITIAL_INFECTIONS) :
		people[i].symptomatic_check()
  
	max_infected_at_once = 0
	max=0
	for i in range (variable.SIM_HOURS):
		max+=1
		num_infected = 0
		num_symptomatic = 0
		num_asymptomatic = 0
		num_immune = 0
		num_dead = 0
		num_vulnerable = 0
		num_incubation = 0
		ui.ui_delete()
		for p in range(variable.NUM_PEOPLE):
			if (not i==0):
				ui.ui_redraw(people[p],int(i/24))
			if (people[p].is_alive()):
				people[p].mobility_model.move()
				people[p].progress_disease()
				if(people[p].status==variable.disease_status.INCUBATION or people[p].status==variable.disease_status.ASYMPTOMATIC or people[p].status==variable.disease_status.SYMPTOMATIC):
					for p2 in range(variable.NUM_PEOPLE):
						if (people[p2].status==variable.disease_status.VULNERABLE):
							people[p].try_infect(people[p2])
			if (not people[p].is_alive()):
				num_dead+=1
			if (people[p].status == variable.disease_status.INCUBATION):
				num_incubation+=1
				num_infected+=1
			if (people[p].status == variable.disease_status.ASYMPTOMATIC):
				num_asymptomatic+=1
				num_infected+=1
			if (people[p].status == variable.disease_status.SYMPTOMATIC):
				num_symptomatic+=1
				num_infected+=1
			if (people[p].status == variable.disease_status.IMMUNE):
				num_immune+=1
			if (people[p].status == variable.disease_status.VULNERABLE):
				num_vulnerable+=1
		ui.ui_refresh()
		if (num_infected > max_infected_at_once):
			max_infected_at_once = num_infected
   
# 	 	#saturated = (num_infected > SATURATION_THRESHOLD);

		if ((i % 24) == 0 and (not num_infected == 0)):
			if (num_dead == 0):
				prob = 0
			else:
				prob = num_dead * 100.0 / (num_immune + num_dead)
			print("Day  ",int(i / 24),"\t",num_vulnerable,"\t\t",num_incubation,"\t\t",num_asymptomatic,"\t\t",num_symptomatic,"\t\t",num_infected,"\t\t\t",num_immune,"\t\t",num_dead,"\t(",prob,"%)\n")
		vulnerable_history[i] = num_vulnerable
		incubation_history[i] = num_incubation
		asymptomatic_history[i] = num_asymptomatic
		symptomatic_history[i] = num_symptomatic
		infected_history[i] = num_infected
		immune_history[i] = num_immune
		dead_history[i] = num_dead
		if (num_infected == 0):
			break
	print("Peak infections : %i\n"% max_infected_at_once)
	print("--- %s seconds ---" % (time.time() - start_time))
	plt.xlim(0,max-1)
	plt.xlabel("Hours #")
	plt.ylabel("Population #")
	plt.axhline(y=max_infected_at_once,color="red",linestyle="--",label="Max Infection")
	plt.plot(vulnerable_history,label="Vulnerable #",lw=3,color='blue')
	plt.plot(incubation_history,label="Incubation #",color="yellow")
	plt.plot(asymptomatic_history,label="Asymptomatic #",color="orange")
	plt.plot(symptomatic_history,label="Sysptomatic #",color="red")
	plt.plot(infected_history,label="Totoal Infected #",lw=3,color="purple")
	plt.plot(immune_history,label="Immune #",lw=3,color="green")
	plt.plot(dead_history,label="Dead #",color="black")
	plt.legend()
	plt.show()