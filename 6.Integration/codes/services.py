# Example code for Services
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ServiceNode(Node):
    def __init__(self):
        super().__init__('service_node')
        self.srv = self.create_service(Trigger, 'reset_map', self.reset_map_callback)

    def reset_map_callback(self, request, response):
        response.success = True
        response.message = 'Map reset successfully.'
        return response

def main(args=None):
    rclpy.init(args=args)
    service_node = ServiceNode()
    rclpy.spin(service_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
