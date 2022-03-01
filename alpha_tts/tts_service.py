import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import os
import sys

class TextToSpeech(Node):
    def __init__(self):
        super().__init__("text_to_speech")



        self._pub = self.create_publisher(msg_type=String, topic="topic", qos_profile=10)

        self.timer = self.create_timer(2, callback=self.do_something)


    
    def do_something(self):
        msg = String()
        msg.data = "hi2you"
        self._pub.publish(msg)
        self.get_logger().info('Publishing : hi2you')
        print("hi")

        os.system('echo "hello world, my name is alpha" | festival --tts')
    #def festival_tts(self, text_request):

        

def main(args=None):

    rclpy.init(args=args)

    node = TextToSpeech()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
