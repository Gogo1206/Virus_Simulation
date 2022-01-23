import random
import mobility_model
import simulation
import person
import location
import variable

popularPlaces = [location.Location()] * variable.NUM_POPULAR_PLACES

for i in range(variable.NUM_POPULAR_PLACES):
    popularPlaces[i] = location.Location()
    popularPlaces[i].random_location()

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
        self.speed = int(random.uniform(10,variable.PP_TOP_SPEED))
        self.stay = int(random.uniform(0,variable.MAX_STAY))
        if(simulation.try_event(self.home_proabilty)):
            self.waypoint=self.home
        else:
            self.waypoint=popularPlaces[int(random.uniform(0,variable.NUM_POPULAR_PLACES))]