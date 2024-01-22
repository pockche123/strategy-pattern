package WithStrategyPattern;

// import WithStrategyPattern.Vehicle;
import WithStrategyPattern.Strategy.SportsDriveStrategy;


public class OffRoadVehicle extends Vehicle {

    OffRoadVehicle(){
        super(new SportsDriveStrategy());
    }
}