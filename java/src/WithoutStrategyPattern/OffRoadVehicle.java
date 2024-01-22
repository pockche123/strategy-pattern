package WithoutStrategyPattern;



public class OffRoadVehicle extends Vehicle{

    @Override
    public void drive(){
        // duplicating the sports driving capability
        System.out.println("sports driving capability");
    }
}