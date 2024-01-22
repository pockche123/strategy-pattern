from vehicle import Vehicle
from strategy.sports_driving_strategy import SportsDrivingStrategy

class OffRoadVehicle(Vehicle): 
    def __init__(self):
        super().__init__(SportsDrivingStrategy())