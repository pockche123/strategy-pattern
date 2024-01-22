package WithStrategyPattern; 

// import WithStrategyPattern.SportsVehicle;

public class Main {

    public static void main(String args[]){
        Vehicle vehicle1 = new SportsVehicle(); 
        vehicle1.drive(); 

        Vehicle offRoad = new OffRoadVehicle(); 
        offRoad.drive();
        // should give you "sports drive capability in the console"
    }
}