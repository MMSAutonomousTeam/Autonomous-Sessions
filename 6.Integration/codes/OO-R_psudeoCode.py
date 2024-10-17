# Sensor Base Class
class Sensor:
    def read_data(self):
        raise NotImplementedError("This method should be overridden.")

# Concrete Sensor Classes
class Camera(Sensor):
    def read_data(self):
        return "Camera data captured."

class LiDAR(Sensor):
    def read_data(self):
        return "LiDAR distance measured."

# Actuator Base Class
class Actuator:
    def activate(self):
        raise NotImplementedError("This method should be overridden.")

# Concrete Actuator Classes
class Motor(Actuator):
    def activate(self):
        return "Motor activated."

class Servo(Actuator):
    def activate(self):
        return "Servo activated."

# Robot Controller
class RobotController:
    def __init__(self):
        self.camera = Camera()
        self.lidar = LiDAR()
        self.motor = Motor()
        self.servo = Servo()

    def perform_action(self):
        print(self.camera.read_data())
        print(self.lidar.read_data())
        print(self.motor.activate())
        print(self.servo.activate())

# Example Usage
if __name__ == "__main__":
    robot = RobotController()
    robot.perform_action()
