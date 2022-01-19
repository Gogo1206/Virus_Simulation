import random
import variable
import person
import location
import ui
#import ui

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
  
	for i in range (variable.NUM_PEOPLE):
		people[i].mask_check()
		people[i].vaccine_check()
  
	for i in range (variable.INITIAL_INFECTIONS) :
		people[i].symptomatic_check()
  
	max_infected_at_once = 0

	for i in range (variable.SIM_HOURS):
		if (not i==0):
			ui.ui_delete()
			for p in range(variable.NUM_PEOPLE):
				ui.ui_redraw(people[p])
			ui.ui_refresh()
		#print(people[1].location.getX()," ",people[1].location.getY(),"-->",people[1].mobility_model.waypoint.getX()," ",people[1].mobility_model.waypoint.getY(),":",people[2].location.getX()," ",people[2].location.getY(),"-->",people[2].mobility_model.waypoint.getX()," ",people[2].mobility_model.waypoint.getY())
		for p in range(variable.NUM_PEOPLE):
			if (people[p].is_alive()):
				people[p].mobility_model.move()
				people[p].progress_disease()
    
		for p in range(variable.NUM_PEOPLE):
			if (people[p].is_alive()):
				for p2 in range(variable.NUM_PEOPLE):
					if ((not p == p2) and people[p2].is_alive() and (not people[p].status==variable.disease_status.VULNERABLE)):
						people[p].try_infect(people[p2])
      
		# for i in range (variable.NUM_PEOPLE):
		# 	print(people[i].location.getX()," ",people[i].location.getY()," ",people[i].status)

		num_infected = 0
		num_symptomatic = 0
		num_asymptomatic = 0
		num_immune = 0
		num_dead = 0
		num_vulnerable = 0
		num_incubation = 0
		for p in range(variable.NUM_PEOPLE):
			# if(not people[p].status==variable.disease_status.VULNERABLE):
			# 	print(people[p].status)
			if (people[p].is_alive()==False):
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
		if (num_infected > max_infected_at_once):
			max_infected_at_once = num_infected
   
	 	#saturated = (num_infected > SATURATION_THRESHOLD);

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