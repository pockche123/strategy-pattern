from strategy.sports_driving_strategy import SportsDrivingStrategy
from vehicle import Vehicle


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDrivingStrategy())