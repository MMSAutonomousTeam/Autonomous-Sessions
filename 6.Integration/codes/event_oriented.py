# Example code for Event-Oriented Execution
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class EventOrientedNode(Node):
    def __init__(self):
        super().__init__('event_oriented_node')
        self.subscriber = self.create_subscription(Image, 'image_topic', self.image_callback, 10)

    def image_callback(self, msg):
        # Code to process the received image
        self.get_logger().info('Image received and processed.')

def main(args=None):
    rclpy.init(args=args)
    event_oriented_node = EventOrientedNode()
    rclpy.spin(event_oriented_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
