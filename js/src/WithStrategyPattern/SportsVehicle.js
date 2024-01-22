
import Vehicle from "./Vehicle.js"
import SportsDriveStrategy from "./Strategy/SportsDriveStrategy.js"

class SportsVehicle extends Vehicle {
    constructor() {
        super(new SportsDriveStrategy())
    }
}

export default SportsVehicle