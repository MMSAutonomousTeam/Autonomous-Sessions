# Example code for Actions
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from example_interfaces.action import Fibonacci

class ActionNode(Node):
    def __init__(self):
        super().__init__('action_node')
        self._action_server = ActionServer(self, Fibonacci, 'fibonacci', self.execute_callback)

    def execute_callback(self, goal_handle):
        feedback_msg = Fibonacci.Feedback()
        for i in range(goal_handle.request.order):
            feedback_msg.sequence.append(i)
            self.get_logger().info(f'Publishing: {feedback_msg.sequence}')
            goal_handle.publish_feedback(feedback_msg)
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.sequence
        return result

def main(args=None):
    rclpy.init(args=args)
    action_node = ActionNode()
    rclpy.spin(action_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
