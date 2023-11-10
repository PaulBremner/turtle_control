#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
import sys
from getkey import getkey, keys
from std_srvs.srv import Empty


def turtle_talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_control', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    msg = Twist()
    lv = 0
    av = 0
    rec_mode = True
    instructions = []
    reset = rospy.ServiceProxy('reset', Empty)
    while not rospy.is_shutdown():

        #lv, av = map(float, raw_input('enter velocity values: ').split())#uncomment to enable input setting values in terminal

        #comment out this section to remove using the arrow keys to alter the velocity
        key = getkey()
        if key == keys.UP:
            lv += 0.1
        elif key == keys.DOWN:
            lv -= 0.1
        elif key == keys.LEFT:
            av -= 0.1
        elif key == keys.RIGHT:
            av += 0.1

        msg.angular.z = float(av)
        msg.linear.x = float(lv)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_talker()
    except rospy.ROSInterruptException:
        pass