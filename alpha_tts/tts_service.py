import rclpy
from rclpy.node import Node

from alpha_interfaces.srv import StringToSpeech


import os
import sys

class TextToSpeech(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(StringToSpeech, 'text_to_speech', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        os.system('echo "' + request.text  + ' " | festival --tts')
        self.get_logger().info('Incoming request : ' + request.text)
        response.result = True

        return response

        

def main(args=None):

    rclpy.init(args=args)

    node = TextToSpeech()
    
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
