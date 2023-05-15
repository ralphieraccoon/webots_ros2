# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""ROS 2 Crazyflie driver."""

import rclpy


class CrazyflieDriver:
    def init(self, webots_node, properties):
        self.robot = webots_node.robot
        self.timestep = int(self.__robot.getBasicTimeStep())

        # ROS interface
        rclpy.init(args=None)
        self.node = rclpy.create_node('crazyflie_driver')


    def step(self):
        rclpy.spin_once(self.node, timeout_sec=0)

