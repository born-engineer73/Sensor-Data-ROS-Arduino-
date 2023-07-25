#!/usr/bin/env python3

import rospy
import os
import numpy as np
from std_msgs.msg import Float32
# global nparray


def joint_state_callback(data):
    print(data)
    # np1=nparray
    nparray.append((data.data))

    
def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('/sensor_data', Float32, joint_state_callback)
    rospy.spin()
    np1=np.array(nparray)
    np.savetxt("firstarray.csv", np1, delimiter=",",fmt='%s')
       


if __name__ == '__main__':   
    global nparray
    nparray=[]
    listener()
    
