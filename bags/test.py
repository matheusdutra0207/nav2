import rclpy 
from rclpy.node import Node

from std_msgs.msg import String
from rosbridge_library.internal.ros_loader import get_message_class


import threading
import time

def ros_thread():
    rclpy.spin(minimal_publisher)

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        # a = self.get_topic_names_and_types()
        # print(a)
        # for topic in a:
        #     print(topic[0])
        #     print(get_message_class(topic[1][0]))  
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    global minimal_publisher
    minimal_publisher = MinimalPublisher()
    thread = threading.Thread(target=ros_thread)
    thread.start()
    
    while True:

        minimal_publisher.timer_callback()
        time.sleep(1)
    


if __name__ == '__main__':
    main()    