import sys

from alpha_interfaces.srv import StringToSpeech
import rclpy
from rclpy.node import Node

class TTSClient(Node):

    def __init__(self) -> None:
        super().__init__('tts_client')
        self.client = self.create_client(StringToSpeech, 'text_to_speech')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Server not availble, waiting...")
        self.request = StringToSpeech.Request()
    
    def send_request(self):
        self.request.text = sys.argv[1]
        self.future = self.client.call_async(self.request)

    
def main(args=None):
    rclpy.init(args=args)

    tts_client = TTSClient()
    tts_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(tts_client)
        if tts_client.future.done():
            try:
                response = tts_client.future.result()
            except Exception as e:
                tts_client.get_logger().info('Service call failed %r' % (e,))
            else:
                tts_client.get_logger().info(f'Service returned:{response.result}')
            break
    
    tts_client.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
