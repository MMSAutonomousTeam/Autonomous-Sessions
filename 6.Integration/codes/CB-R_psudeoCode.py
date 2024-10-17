# Sensor Node
class SensorNode:
    def __init__(self, topic_name):
        self.topic_name = topic_name
        self.data = None

    def publish_data(self, data):
        self.data = data

# Actuator Node
class ActuatorNode:
    def __init__(self, topic_name):
        self.topic_name = topic_name

    def process_data(self, data):
        # Perform action based on received data
        print("Received data:", data)

# Message Broker
class MessageBroker:
    def __init__(self):
        self.topics = {}

    def publish(self, topic_name, data):
        if topic_name in self.topics:
            for component in self.topics[topic_name]:
                component.process_data(data)

    def subscribe(self, topic_name, component):
        if topic_name not in self.topics:
            self.topics[topic_name] = []
        self.topics[topic_name].append(component)

# Robot Controller
class RobotController:
    def __init__(self):
        self.message_broker = MessageBroker()

        self.camera_node = SensorNode('/camera_data')
        self.lidar_node = SensorNode('/lidar_data')
        self.motor_node = ActuatorNode('/motor_control')
        self.servo_node = ActuatorNode('/servo_control')

        self.message_broker.subscribe('/camera_data', self.motor_node)
        self.message_broker.subscribe('/lidar_data', self.servo_node)

    def run(self):
        while True:
            camera_data = "Camera data captured"
            lidar_data = "LiDAR distance measured"

            self.message_broker.publish('/camera_data', camera_data)
            self.message_broker.publish('/lidar_data', lidar_data)

if __name__ == '__main__':
    robot_controller = RobotController()
    robot_controller.run()