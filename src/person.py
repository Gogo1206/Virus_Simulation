import random
import simulation
import variable
import ppmodel
import location

class Person():
    def __init__(self):
        self.mobility_model = ppmodel.PopularPlacesModel()
        self.mobility_model.setPerson(self)
        self.location = location.Location()
        self.status = variable.disease_status.VULNERABLE
        self.masked = False
        self.vaccinated = False
        self.disease_counter = 0
        self.incubation_counter = int(random.uniform(0,variable.MAX_INCUBATION_TIME))
    def infect(self):
        if(self.status==variable.disease_status.VULNERABLE):
            self.status=variable.disease_status.INCUBATION
            return True
        else:
            return False
    def try_infect(self,other_person):
        if(not other_person.status==variable.disease_status.VULNERABLE):
            return False
        if(self.location.get_distance(other_person.location)>variable.INFECTION_PROXIMITY):
            return False
        if(other_person.location.at_location(other_person.mobility_model.home)):
            if(simulation.try_event(variable.HOME_INFECTTION_PROBABILTY)):
                return other_person.infect()
        if(other_person.masked and other_person.vaccinated):
            if(simulation.try_event(variable.MASKED_VACCINEATED_INFECTTION_PROBABILTY)):
                return other_person.infect()
        if(other_person.masked):
            if(simulation.try_event(variable.MASKED_INFECTTION_PROBABILTY)):
                return other_person.infect()
        if(other_person.vaccinated):
            if(simulation.try_event(variable.VACCINEATED_INFECTTION_PROBABILTY)):
                return other_person.infect()
        if(simulation.try_event(variable.NORMAL_INFECTTION_PROBABILTY)):
            return other_person.infect()
        return False
    def symptomatic_check(self):
        if(self.vaccinated):
            if(simulation.try_event(variable.VACCINEATED_ASYMPTOMATIC_PROBABILTY)):
                self.status=variable.disease_status.ASYMPTOMATIC
                self.disease_counter = int(random.uniform(24*7,variable.MAX_ASYMPTOMATIC_INFECTION_TIME))
            else:
                self.status=variable.disease_status.SYMPTOMATIC
                self.disease_counter = int(random.uniform(24*3,variable.MAX_SYMPTOMATIC_INFECTION_TIME))
        else:
            if (simulation.try_event(variable.NORMAL_ASYMPTOMATIC_PROBABILTY)):
                self.status=variable.disease_status.ASYMPTOMATIC
                self.disease_counter = int(random.uniform(24*7,variable.MAX_ASYMPTOMATIC_INFECTION_TIME))
            else:
                self.status=variable.disease_status.SYMPTOMATIC
                self.disease_counter = int(random.uniform(24*3,variable.MAX_SYMPTOMATIC_INFECTION_TIME))
    def mask_check(self):
        if(simulation.try_event(variable.MASKING_PERCENTAGE)):
            self.masked = True
        else:
            self.masked = False
    def vaccine_check(self):
        if(simulation.try_event(variable.VACCINATION_PERCENTAGE)):
            self.vaccinated = True
        else:
            self.vaccinated = False
    def progress_disease(self):
        if(self.status == variable.disease_status.INCUBATION):
            self.incubation_counter-=1
            if(self.incubation_counter<=0):
                self.symptomatic_check()
        if(self.status==variable.disease_status.ASYMPTOMATIC or self.status==variable.disease_status.SYMPTOMATIC):
            self.disease_counter-=1
            if(self.disease_counter<=0):
                if(self.status==variable.disease_status.SYMPTOMATIC):
                    if(simulation.try_event(variable.NORMAL_FATALITY_RATE)):
                        self.status=variable.disease_status.DEAD
                        return
                elif(self.status==variable.disease_status.ASYMPTOMATIC):
                    if(simulation.try_event(variable.ASYMPTOMATIC_FATALITY_RATE)):
                        self.status=variable.disease_status.DEAD
                        return
                self.status=variable.disease_status.IMMUNE
    def is_alive(self):
        return not self.status ==variable.disease_status.DEAD