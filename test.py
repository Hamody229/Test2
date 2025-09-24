#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  #MODIFY TYPE

class PublisherNode(Node): #MODIFY NAME
    def __init__(self):
        super().__init__('minimal_publisher')

        self.publisher_ = self.create_publisher(String, 'topic', 10) # MODIFY TOPIC AND TYPE

        timer_period = 1.0  #MODIFY TIMER RATE 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS2: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
