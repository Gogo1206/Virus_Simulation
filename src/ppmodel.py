import random
import mobility_model
import simulation
import person
import location
import variable

popularPlaces = []

xi = 1
yi = 1

# for i in range(variable.NUM_POPULAR_PLACES):
#     new_place = location.Location()
#     new_place.random_location()
#     popularPlaces.append(new_place)
for xi in range(0, 5):
    for yi in range(0, 4):
        new_place = location.Location()
        new_place.location(250+xi*1750,250+yi*2333)
        popularPlaces.append(new_place)

class PopularPlacesModel(mobility_model.MobilityModel):
    def __init__(self):
        self.waypoint = location.Location()
        self.waypoint.random_location()
        self.speed = -1
        self.stay = 0
        self.home = location.Location()
        self.home.random_location()
        if(simulation.try_event(variable.DISTANCING_PROBABILITY)):
            self.home_proabilty = variable.DISTANCING_HOME_PROBABILITY
        else:
            self.home_proabilty = variable.NOT_DISTANCING_HOME_PROBABILITY
    def move(self):
        if(self.speed < 0):
            self.person.location.setX(self.home.getX())
            self.person.location.setY(self.home.getY())
            self.pick_new_waypoint()
        elif(self.person.location.at_location(self.waypoint)):
            self.stay-=1
            if(self.stay<=0):
                self.pick_new_waypoint()
        else:
            self.person.location.move_toward(self.waypoint,self.speed)
    def pick_new_waypoint(self):
        self.speed = random.uniform(10,variable.PP_TOP_SPEED)
        self.stay = random.randint(0,variable.MAX_STAY)
        if(simulation.try_event(self.home_proabilty)):
            self.waypoint=self.home
        else:
            self.waypoint=popularPlaces[random.randint(0,variable.NUM_POPULAR_PLACES-1)]