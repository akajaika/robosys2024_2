#!/usr/bin/env python
# SPDX-FileCopyrightText: 2025 Kai Nonaka
# SPDX-License-Identifier: BSD-3-Clause:

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String

class SimilarityListener(Node):
    def __init__(self):
        super().__init__('similarity_listener')
        self.create_subscription(Float32MultiArray, 'similar', self.similarity_callback, 10)
        self.create_subscription(String, 'file_names', self.filenames_callback, 10)
        self.received_data1 = False  
        self.received_data2 = False  

    def similarity_callback(self, msg):
        if not self.received_data1:  # 最初の受信時にのみ処理を実行
            self.get_logger().info(f"Received similarity data: {msg.data}")
            self.received_data1 = True  

    def filenames_callback(self, msg):
        if not self.received_data2:  # 最初の受信時にのみ処理を実行
            self.get_logger().info(f"Received filenames: {msg.data}")
            self.received_data2 = True  

def main():
    rclpy.init()
    node = SimilarityListener()

    while not (node.received_data1 and node.received_data2):  
        rclpy.spin_once(node)  
    
    # ノードシャットダウンの方法を修正
    rclpy.shutdown()  

if __name__ == '__main__':
    main()
