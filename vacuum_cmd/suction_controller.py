#!/usr/bin/env python3
import rospy
import numpy as np
import pyfirmata
from std_msgs.msg import Int32MultiArray


class SuctionOperator:
    def __init__(self):
        rospy.init_node('suction_operator')
        self.suction_status = np.zeros(6).astype(int)
        
        board = pyfirmata.Arduino('/dev/ttyACM0')
        self.suction_pin = [board.get_pin('d:3:p'), board.get_pin('d:5:p'), board.get_pin('d:6:p'),  board.get_pin('d:9:p'), board.get_pin('d:10:p'), board.get_pin('d:11:p')]
        
        rospy.Subscriber('/unld/vacuum_cmd', Int32MultiArray, self.suction_cb)
        self.status_pub = rospy.Publisher('/unld/vacuum_state', Int32MultiArray, queue_size=10)

        it = pyfirmata.util.Iterator(board)
        it.start()
        
        rospy.Timer(rospy.Duration(0.1), self.suction_operator)
        rospy.Timer(rospy.Duration(0.1), self.suction_status_publisher)


    def suction_cb(self, data):

        for i, tf in enumerate(data.data):
            self.suction_status[i] = tf


    def suction_operator(self, event):
        for i, tf in enumerate(self.suction_status):
            self.suction_pin[i].write(tf)


    def suction_status_publisher(self, event):
        msg = Int32MultiArray()
        for tf in self.suction_status:            
            msg.data.append(tf)
        self.status_pub.publish(msg)


if __name__ == '__main__':
    SO = SuctionOperator()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass