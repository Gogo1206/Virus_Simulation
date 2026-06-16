class MobilityModel:
    """Base class for person mobility models."""

    def __init__(self):
        self.person = None

    def setPerson(self, p):
        """Set the person this mobility model controls."""
        self.person = p
