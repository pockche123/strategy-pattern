# from with_strategy_pattern.offroad_vehicle import OffRoadVehicle
from offroad_vehicle import OffRoadVehicle
from sports_vehicle import SportsVehicle
from strategy.sports_driving_strategy import SportsDrivingStrategy
from strategy.normal_driving_strategy import NormalDrivingStrategy
from  vehicle import Vehicle

def main():
    
    normal_vehicle = Vehicle(NormalDrivingStrategy())
    normal_vehicle.drive()
    
    sports_car = SportsVehicle()
    sports_car.drive()
    
    offroad_car = OffRoadVehicle()
    offroad_car.drive()
    
    
    
    


if __name__ == "__main__":
    main()