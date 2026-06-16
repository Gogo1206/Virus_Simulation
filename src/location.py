import math
import random

import variable


class Location:
    """2D coordinate with movement and distance helpers."""

    def __init__(self):
        self.x = 0
        self.y = 0

    def random_location(self):
        """Set position to a random coordinate within simulation bounds."""
        self.x = int(random.uniform(0, variable.X_LIMIT))
        self.y = int(random.uniform(0, variable.Y_LIMIT))

    def location(self, nx, ny):
        """Set position to the given coordinates."""
        self.x = nx
        self.y = ny

    def move_toward(self, destination, howfar):
        """Move toward destination by howfar units. Returns True if arrived."""
        dx = destination.x - self.x
        dy = destination.y - self.y
        theta = math.atan2(dy, dx)

        distance = math.sqrt((dx * dx) + (dy * dy))

        if distance < howfar:
            self.x = destination.x
            self.y = destination.y
            return True
        else:
            self.x = self.x + howfar * math.cos(theta)
            self.y = self.y + howfar * math.sin(theta)
            return False

    def get_distance(self, other_location):
        """Return Euclidean distance to another location."""
        dx = other_location.x - self.x
        dy = other_location.y - self.y
        return math.sqrt((dx * dx) + (dy * dy))

    def at_location(self, destination):
        """Return True if within CLOSE_ENOUGH of the destination."""
        return self.get_distance(destination) < variable.CLOSE_ENOUGH

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, nx):
        self.x = nx

    def setY(self, ny):
        self.y = ny
