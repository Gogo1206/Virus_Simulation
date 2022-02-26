import random
from time import sleep

from numpy import average
import variable
import person
import ui
import time
import sir
import excel

start_time = time.time()

def try_event(probability):
	'''try event with given probability'''
	rnum = (int(random.uniform(0,100))+1)/100
	return rnum <= probability


def sim_main():
	'''start simulation'''
    #set initial variables to store data
	vulnerable_history = [] 
	incubation_history = []
	asymptomatic_history = []
	symptomatic_history = []
	infected_history = []
	immune_history = []
	dead_history = []
	max_infected_at_once = 0
	hours_past = 0
	people = []

	#initialize population
	for i in range (variable.NUM_PEOPLE):
		new_person=person.Person()
		new_person.mask_check()
		new_person.vaccine_check()
		people.append(new_person)

	#set initial infection individuals
	for i in range (variable.INITIAL_INFECTIONS):
		people[i].symptomatic_check()
		people[i].infection_level=0
	
	#print lable
	print("Day  #\t\tVulnerable #\tIncubation #\tAsymptomatic #\tSymptomatic #\tTotal Infected #\tImmune #\tDead #\t(Death rate in %)\n")
 	
	#start simulation (i represent hours passed)
	for i in range (variable.SIM_HOURS):
		check_infected = True
		if(not i == 0):
			if(num_infected>num_vulnerable):
				check_infected = False
		hours_past+=1
		num_infected = 0
		num_symptomatic = 0
		num_asymptomatic = 0
		num_immune = 0
		num_dead = 0
		num_vulnerable = 0
		num_incubation = 0
		ui.ui_delete()
		ui.draw_popularPlace()

		#simulation for every individual
		for p in people:
			if (p.is_alive()):
				p.mobility_model.move()
				p.progress_disease()
			if(check_infected):
				if(p.status==variable.disease_status.INCUBATION or p.status==variable.disease_status.ASYMPTOMATIC or p.status==variable.disease_status.SYMPTOMATIC):
					for p2 in people:
						if (p2.status==variable.disease_status.VULNERABLE):
							p.try_infect(p2)
			else:
				if(p.status==variable.disease_status.VULNERABLE):
					for p2 in people:
						if (p2.status==variable.disease_status.INCUBATION or p2.status==variable.disease_status.ASYMPTOMATIC or p2.status==variable.disease_status.SYMPTOMATIC):
							p2.try_infect(p)
			if (not p.is_alive()):
				num_dead+=1
			if (p.status == variable.disease_status.INCUBATION):
				num_incubation+=1
				num_infected+=1
			if (p.status == variable.disease_status.ASYMPTOMATIC):
				num_asymptomatic+=1
				num_infected+=1
			if (p.status == variable.disease_status.SYMPTOMATIC):
				num_symptomatic+=1
				num_infected+=1
			if (p.status == variable.disease_status.IMMUNE):
				num_immune+=1
			if (p.status == variable.disease_status.VULNERABLE):
				num_vulnerable+=1
			if (not i==0):
				ui.ui_redraw(p,int(i/24))
		ui.ui_refresh()
		if (num_infected > max_infected_at_once):
			max_infected_at_once = num_infected

		#print out data for every day passed
		if ((i % 24) == 0 or num_infected == 0):
			ui.print_graph(hours_past,max_infected_at_once,vulnerable_history,incubation_history,asymptomatic_history,symptomatic_history,infected_history,immune_history,dead_history)
			if (num_dead == 0):
				prob = 0
			else:
				prob = num_dead * 100.0 / (num_immune + num_dead)
			print("Day  ",int(i / 24),"\t",num_vulnerable,"\t\t",num_incubation,"\t\t",num_asymptomatic,"\t\t",num_symptomatic,"\t\t",num_infected,"\t\t\t",num_immune,"\t\t",num_dead,"\t(",prob,"%)\n")
		
		#store data for every hour
		dead_history.append(num_dead)
		vulnerable_history.append(num_vulnerable)
		incubation_history.append(num_incubation)
		asymptomatic_history.append(num_asymptomatic)
		symptomatic_history.append(num_symptomatic)
		infected_history.append(num_infected)
		immune_history.append(num_immune)
		dead_history.append(num_dead)
		# excel.write(i+1,0,i)
		# excel.write(i+1,1,num_vulnerable)
		# excel.write(i+1,2,num_infected)
		# excel.write(i+1,3,num_immune)
		if (num_infected == 0):
			break

	print("Hours ran: ",hours_past)
	print("Peak infection: %i"% max_infected_at_once)

	print("--- %s seconds ---" % (time.time() - start_time))
	sir.cal_infection_rate(people,hours_past)
	ui.end()