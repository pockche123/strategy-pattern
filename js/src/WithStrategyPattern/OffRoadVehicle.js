import Vehicle from "./Vehicle.js"
import SportsDriveStrategy from "./Strategy/SportsDriveStrategy.js"

class OffRoadVehicle extends Vehicle {
    constructor() {
        super(new SportsDriveStrategy())
    }
}

export default OffRoadVehicle