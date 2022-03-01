import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__("minimal_publisher")

        self._pub = self.create_publisher(msg_type=String, topic="topic", qos_profile=10)

        self.timer = self.create_timer(0.5, callback=self.do_something)

    
    def do_something(self):
        msg = String()
        msg.data = "hi2you"
        self._pub.publish(msg)
        self.get_logger().info('Publishing : hi2you')
        print("hi")

def main(args=None):

    rclpy.init(args=args)

    node = MinimalPublisher()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
