import OffRoadVehicle from "./OffRoadVehicle.js"
import SportsVehicle from "./SportsVehicle.js"

const myOffRoadVehicle = new OffRoadVehicle()
myOffRoadVehicle.drive()

const sportsCar = new SportsVehicle()
sportsCar.drive()
// both should output "sports driving capability"