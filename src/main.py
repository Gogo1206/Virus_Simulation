import variable
import person
import simulation
import ui

def main():
	#x = 0
	#y = 0
	#for j in range(100):
	#	a = 0
	#	b = 0
	#	for i in range(1000):
	#		if (try_event(0.05))
	#			a+=1
	#		else:
	#			b+=1
	#	print(a," ",b)
	#	if (a / 10000.0 > 0.05):
	#		x+=1
	#	else:
	#		y+=1
	#print(x," ",y)
	print("Day  #\t\tVulnerable #\tIncubation #\tAsymptomatic #\tSymptomatic #\tTotal Infected #\tImmune #\tDead #\t(Death rate in %)\n")
	# a = Location()
	# a.location(0,0)
	# b = Location()
	# b.location(5,5)
	# print(Location.get_distance(a,b))
	# for i in ppmodel.popularPlaces:
	# 	print(i.getX()," ",i.getY())
	# a = Person()
	# print(a.status)
	# print(a.status==disease_status.VULNERABLE)
	ui.start_ui()
	simulation.sim_main()
 
main()