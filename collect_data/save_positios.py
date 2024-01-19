import sys
import pandas as pd

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovariance, PoseWithCovarianceStamped
from nav_msgs.msg import Odometry


class MinimalSubscriber(Node):

    def __init__(self, consume_list, df_data, data_id):
        super().__init__('Collect')
        self.df_data = df_data
        self.data_id = data_id
        
        if "amcl" in consume_list:
            self.subscription = self.create_subscription(
                PoseWithCovarianceStamped,
                'amcl_pose',
                self.callback_amcl,
                10)

    def callback_amcl(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        yaw = msg.pose.pose.orientation.z
        self.df_data['amcl']['x'].append(x)
        self.df_data['amcl']['y'].append(y)
        self.df_data['amcl']['yaw'].append(yaw)
        self.save_data(self.df_data, self.data_id)
        self.get_logger().info("new pose amcl")
  
    def save_data(self, df_data, data_id):
        df_data.to_csv(f'datas/data{data_id}.csv', index=False)
        self.get_logger().info("new data saved")


def main(args=None):
    data_id = int(sys.argv[1])
    aruco_id = 5
    consume_list = sys.argv[2:]
    position_data = {}
    if 'amcl' in consume_list:
        position_data['amcl'] = {'x': [], 'y': [], 'yaw': []}
    if 'ekf' in consume_list:
        position_data['ekf'] = {'x': [], 'y': [], 'yaw': []}
    if 'vo' in consume_list:
        position_data['vo'] = {'x': [], 'y': [], 'yaw': []}      

    df_data = pd.DataFrame.from_dict(position_data)      

    rclpy.init(args=args)


    minimal_subscriber = MinimalSubscriber(
                            consume_list,
                            df_data,
                            data_id
                            )

    rclpy.spin(minimal_subscriber)
    save_data(df_data)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
