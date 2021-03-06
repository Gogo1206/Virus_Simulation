import enum

#stages of disease
class disease_status(enum.Enum):
    VULNERABLE = 0
    INCUBATION = 1
    ASYMPTOMATIC = 2
    SYMPTOMATIC = 3
    IMMUNE = 4
    DEAD = 5

#simulation variables
X_LIMIT = 7500
Y_LIMIT = 7500
NUM_PEOPLE = 1000
SIM_HOURS = 5000
INITIAL_INFECTIONS = 5
SATURATION_THRESHOLD = (NUM_PEOPLE/5)

#disease variable
MAX_SYMPTOMATIC_INFECTION_TIME = (24*14)
MAX_ASYMPTOMATIC_INFECTION_TIME = (24*7)
MAX_INCUBATION_TIME = (24*7)

NORMAL_INFECTTION_PROBABILTY = 0.7
MASKED_INFECTTION_PROBABILTY = 0.3
VACCINATED_INFECTTION_PROBABILTY = 0.3
MASKED_VACCINATED_INFECTTION_PROBABILTY = 0.1
HOME_INFECTTION_PROBABILTY = 0
NORMAL_FATALITY_RATE = 0.02
ASYMPTOMATIC_FATALITY_RATE = 0
# SATURATED_FATALITY_RATE = 0.06
INFECTION_PROXIMITY = 15

#population variables
NORMAL_ASYMPTOMATIC_PROBABILTY = 0.2
VACCINATED_ASYMPTOMATIC_PROBABILTY = 0.4
MASKING_PERCENTAGE = 0.5
VACCINATION_PERCENTAGE = 0.5

#"location" variables
CLOSE_ENOUGH = 0.05

#"ppmodel" variables
NUM_POPULAR_PLACES = 20
DISTANCING_PROBABILITY = 0.3
DISTANCING_HOME_PROBABILITY = 0.5
NOT_DISTANCING_HOME_PROBABILITY = 0.2

PP_TOP_SPEED = 20
MAX_STAY = 2*24

#variables to add in future
#temperture