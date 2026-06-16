import random

import simulation
import variable
import ppmodel
import location


class Person:
    """Individual agent in the virus simulation with disease state and behavior."""

    def __init__(self):
        self.mobility_model = ppmodel.PopularPlacesModel()
        self.mobility_model.setPerson(self)
        self.location = location.Location()
        self.status = variable.DiseaseStatus.VULNERABLE
        self.masked = False
        self.vaccinated = False
        self.disease_counter = 0
        self.incubation_counter = random.randint(
            0, variable.MAX_INCUBATION_TIME)
        self.infected = 0
        self.infection_level = -1

    def infect(self):
        """Try to infect this person. Returns True if infection succeeded."""
        if self.status == variable.DiseaseStatus.VULNERABLE:
            self.status = variable.DiseaseStatus.INCUBATION
            return True
        return False

    def try_infect(self, other_person):
        """Attempt to infect another person based on proximity and protections."""
        if (self.location.get_distance(other_person.location)
                > variable.INFECTION_PROXIMITY):
            return False
        if (other_person.location.at_location(other_person.mobility_model.home)
                or self.location.at_location(self.mobility_model.home)):
            if simulation.try_event(variable.HOME_INFECTTION_PROBABILTY):
                self.infected += 1
                other_person.infection_level = self.infection_level + 1
                return other_person.infect()
        if other_person.masked and other_person.vaccinated:
            if simulation.try_event(
                    variable.MASKED_VACCINATED_INFECTTION_PROBABILTY):
                self.infected += 1
                other_person.infection_level = self.infection_level + 1
                return other_person.infect()
        if other_person.masked:
            if simulation.try_event(variable.MASKED_INFECTTION_PROBABILTY):
                self.infected += 1
                other_person.infection_level = self.infection_level + 1
                return other_person.infect()
        if other_person.vaccinated:
            if simulation.try_event(variable.VACCINATED_INFECTTION_PROBABILTY):
                self.infected += 1
                other_person.infection_level = self.infection_level + 1
                return other_person.infect()
        if simulation.try_event(variable.NORMAL_INFECTTION_PROBABILTY):
            self.infected += 1
            other_person.infection_level = self.infection_level + 1
            return other_person.infect()
        return False

    def symptomatic_check(self):
        """Determine whether infected person becomes symptomatic or asymptomatic."""
        if self.vaccinated:
            if simulation.try_event(
                    variable.VACCINATED_ASYMPTOMATIC_PROBABILTY):
                self.status = variable.DiseaseStatus.ASYMPTOMATIC
                self.disease_counter = random.randint(
                    24 * 3, variable.MAX_ASYMPTOMATIC_INFECTION_TIME)
            else:
                self.status = variable.DiseaseStatus.SYMPTOMATIC
                self.disease_counter = random.randint(
                    24 * 3, variable.MAX_SYMPTOMATIC_INFECTION_TIME)
        else:
            if simulation.try_event(variable.NORMAL_ASYMPTOMATIC_PROBABILTY):
                self.status = variable.DiseaseStatus.ASYMPTOMATIC
                self.disease_counter = random.randint(
                    24 * 3, variable.MAX_ASYMPTOMATIC_INFECTION_TIME)
            else:
                self.status = variable.DiseaseStatus.SYMPTOMATIC
                self.disease_counter = random.randint(
                    24 * 3, variable.MAX_SYMPTOMATIC_INFECTION_TIME)

    def mask_check(self):
        """Randomly assign mask based on MASKING_PERCENTAGE."""
        if simulation.try_event(variable.MASKING_PERCENTAGE):
            self.masked = True
        else:
            self.masked = False

    def vaccine_check(self):
        """Randomly assign vaccine based on VACCINATION_PERCENTAGE."""
        if simulation.try_event(variable.VACCINATION_PERCENTAGE):
            self.vaccinated = True
        else:
            self.vaccinated = False

    def progress_disease(self):
        """Advance disease state by one hour."""
        if self.status == variable.DiseaseStatus.INCUBATION:
            self.incubation_counter -= 1
            if self.incubation_counter <= 0:
                self.symptomatic_check()
        if (self.status == variable.DiseaseStatus.ASYMPTOMATIC
                or self.status == variable.DiseaseStatus.SYMPTOMATIC):
            self.disease_counter -= 1
            if self.disease_counter <= 0:
                if self.status == variable.DiseaseStatus.SYMPTOMATIC:
                    if simulation.try_event(variable.NORMAL_FATALITY_RATE):
                        self.status = variable.DiseaseStatus.DEAD
                        return
                elif self.status == variable.DiseaseStatus.ASYMPTOMATIC:
                    if simulation.try_event(variable.ASYMPTOMATIC_FATALITY_RATE):
                        self.status = variable.DiseaseStatus.DEAD
                        return
                self.status = variable.DiseaseStatus.IMMUNE

    def is_alive(self):
        """Return True if person is not dead."""
        return self.status != variable.DiseaseStatus.DEAD
