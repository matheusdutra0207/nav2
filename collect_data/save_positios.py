import sys
import pandas as pd
import csv


import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry


class MinimalSubscriber(Node):

    def __init__(self, consume_list, df_data, data_id):
        super().__init__("Collect")
        self.df_data = df_data
        self.data_id = data_id

        if "amcl" in consume_list:
            self.subscription = self.create_subscription(
                PoseWithCovarianceStamped, "amcl_pose", self.callback_amcl, 10
            )
        if "vo" in consume_list:
            self.subscription = self.create_subscription(
                PoseWithCovarianceStamped, "vo", self.callback_vo, 10
            )
        if "ekf" in consume_list:
            self.subscription = self.create_subscription(
                Odometry, "/odometry/filtered", self.callback_ekf, 10
            )

    def callback_amcl(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        x_theta = msg.pose.pose.orientation.x
        y_theta = msg.pose.pose.orientation.y
        z_theta = msg.pose.pose.orientation.z
        w = y_theta = msg.pose.pose.orientation.w
        self.df_data["amcl"]["x"].append(x)
        self.df_data["amcl"]["y"].append(y)
        self.df_data["amcl"]["x_theta"].append(x_theta)
        self.df_data["amcl"]["y_theta"].append(y_theta)
        self.df_data["amcl"]["z_theta"].append(z_theta)
        self.df_data["amcl"]["w"].append(w)
        self.save_data(self.df_data, self.data_id)
        self.get_logger().info("new pose amcl")

    def callback_vo(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        x_theta = msg.pose.pose.orientation.x
        y_theta = msg.pose.pose.orientation.y
        z_theta = msg.pose.pose.orientation.z
        w = y_theta = msg.pose.pose.orientation.w
        self.df_data["vo"]["x"].append(x)
        self.df_data["vo"]["y"].append(y)
        self.df_data["vo"]["x_theta"].append(x_theta)
        self.df_data["vo"]["y_theta"].append(y_theta)
        self.df_data["vo"]["z_theta"].append(z_theta)
        self.df_data["vo"]["w"].append(w)
        self.save_data(self.df_data, self.data_id)
        self.get_logger().info("new pose vo")

    def callback_ekf(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        x_theta = msg.pose.pose.orientation.x
        y_theta = msg.pose.pose.orientation.y
        z_theta = msg.pose.pose.orientation.z
        w = y_theta = msg.pose.pose.orientation.w
        self.df_data["ekf"]["x"].append(x)
        self.df_data["ekf"]["y"].append(y)
        self.df_data["ekf"]["x_theta"].append(x_theta)
        self.df_data["ekf"]["y_theta"].append(y_theta)
        self.df_data["ekf"]["z_theta"].append(z_theta)
        self.df_data["ekf"]["w"].append(w)
        self.save_data(self.df_data, self.data_id)
        self.get_logger().info("new pose ekf")

    def save_data(self, df_data, data_id):
        with open(f"datas/data{data_id}.csv", "w") as f:
            w = csv.DictWriter(f, df_data.keys())
            w.writeheader()
            w.writerow(df_data)
            # df_data.to_csv(f"datas/data{data_id}.csv", index=False)
            self.get_logger().info("new data saved")
            print(df_data)


def main(args=None):
    data_id = int(sys.argv[1])
    consume_list = sys.argv[2:]
    df = {
        "amcl": {
            "x": [],
            "y": [],
            "x_theta": [],
            "y_theta": [],
            "z_theta": [],
            "w": [],
        },
        "ekf": {
            "x": [],
            "y": [],
            "x_theta": [],
            "y_theta": [],
            "z_theta": [],
            "w": [],
        },
        "vo": {
            "x": [],
            "y": [],
            "x_theta": [],
            "y_theta": [],
            "z_theta": [],
            "w": [],
        },
    }

    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber(consume_list, df, data_id)

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
