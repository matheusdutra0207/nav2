import rclpy
from rclpy.node import Node

import numpy as np

from geometry_msgs.msg import PoseWithCovarianceStamped


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__("minimal_subscriber")
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped, "vo", self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(
            PoseWithCovarianceStamped, "vo_pipe", 10
        )

    def timer_callback(self, msg):
        measurement_covariance_noise = 0.00009
        msg.pose.covariance = np.array(
            [
                measurement_covariance_noise,
                0,
                0,
                0,
                0,
                0,
                0,
                measurement_covariance_noise,
                0,
                0,
                0,
                0,
                0,
                0,
                measurement_covariance_noise,
                0,
                0,
                0,
                0,
                0,
                0,
                measurement_covariance_noise,
                0,
                0,
                0,
                0,
                0,
                0,
                measurement_covariance_noise,
                0,
                0,
                0,
                0,
                0,
                0,
                measurement_covariance_noise,
            ]
        )
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg)
        self.timer_callback(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
