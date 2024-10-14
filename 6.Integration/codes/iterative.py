# Example code for Iterative Execution
import rclpy
from rclpy.node import Node

class IterativeNode(Node):
    def __init__(self):
        super().__init__('iterative_node')
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20 Hz

    def timer_callback(self):
        # Code to calculate motion commands
        self.get_logger().info('Motion command calculated.')

def main(args=None):
    rclpy.init(args=args)
    iterative_node = IterativeNode()
    rclpy.spin(iterative_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
