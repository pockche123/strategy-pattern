import DriveStrategy from "./DriveStrategy.js"

class NormalDriveStrategy extends DriveStrategy{
    drive() {
        console.log("normal driving capability")
    }
}

export default NormalDriveStrategy