from strategy.drive_strategy import DriveStrategy

class Vehicle:
    def __init__(self, drive_obj: DriveStrategy):
        self.drive_object = drive_obj
        
    def drive(self):
        self.drive_object.drive()