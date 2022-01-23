import variable
import person
import simulation
import ui

def main():
	print("Day  #\t\tVulnerable #\tIncubation #\tAsymptomatic #\tSymptomatic #\tTotal Infected #\tImmune #\tDead #\t(Death rate in %)\n")
	ui.start_ui()
	simulation.sim_main()

main()