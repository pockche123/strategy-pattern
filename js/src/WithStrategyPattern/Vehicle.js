
class Vehicle {
    constructor(driveObj) {
        this.driveObject = driveObj
    }

    drive() {
        this.driveObject.drive()
    }
}

export default Vehicle