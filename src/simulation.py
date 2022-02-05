import random
from time import sleep
import variable
import person
import ui
import time

start_time = time.time()

#try event with given probability
def try_event(probability):
	rnum = (int(random.uniform(0,100))+1)/100
	return rnum <= probability

#simulation
def sim_main():
    #set initial variables to store data
	vulnerable_history = [0] * variable.SIM_HOURS
	incubation_history = [0] * variable.SIM_HOURS
	asymptomatic_history = [0] * variable.SIM_HOURS
	symptomatic_history = [0] * variable.SIM_HOURS
	infected_history = [0] * variable.SIM_HOURS
	immune_history = [0] * variable.SIM_HOURS
	dead_history = [0] * variable.SIM_HOURS
	max_infected_at_once = 0
	max_day=0

	#initialize the population
	people = [person.Person()] * variable.NUM_PEOPLE

	#saturated = false;

	#initialize individual's protection method
	for i in range (variable.NUM_PEOPLE):
		people[i] = person.Person()
		people[i].mask_check()
		people[i].vaccine_check()

	#set initial infection individuals
	for i in range (variable.INITIAL_INFECTIONS) :
		people[i].symptomatic_check()
	
	#print lable
	print("Day  #\t\tVulnerable #\tIncubation #\tAsymptomatic #\tSymptomatic #\tTotal Infected #\tImmune #\tDead #\t(Death rate in %)\n")	

	#start simulation (i represent hours passed)
	for i in range (variable.SIM_HOURS):
		max_day+=1
		num_infected = 0
		num_symptomatic = 0
		num_asymptomatic = 0
		num_immune = 0
		num_dead = 0
		num_vulnerable = 0
		num_incubation = 0
		ui.ui_delete()

		#simulation for every individual
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
   
 	 	#saturated = (num_infected > SATURATION_THRESHOLD);

		#print out data for every day passed
		if ((i % 24) == 0 and (not num_infected == 0)):
			if (num_dead == 0):
				prob = 0
			else:
				prob = num_dead * 100.0 / (num_immune + num_dead)
			print("Day  ",int(i / 24),"\t",num_vulnerable,"\t\t",num_incubation,"\t\t",num_asymptomatic,"\t\t",num_symptomatic,"\t\t",num_infected,"\t\t\t",num_immune,"\t\t",num_dead,"\t(",prob,"%)\n")
		
		#store data for every hour
		vulnerable_history[i] = num_vulnerable
		incubation_history[i] = num_incubation
		asymptomatic_history[i] = num_asymptomatic
		symptomatic_history[i] = num_symptomatic
		infected_history[i] = num_infected
		immune_history[i] = num_immune
		dead_history[i] = num_dead
		if (num_infected == 0):
			break
	
	#print data collected after simulation is finished
	print("Peak infections : %i\n"% max_infected_at_once)
	print("--- %s seconds ---" % (time.time() - start_time))
	ui.print_graph(max_day,max_infected_at_once,vulnerable_history,incubation_history,asymptomatic_history,symptomatic_history,infected_history,immune_history,dead_history)