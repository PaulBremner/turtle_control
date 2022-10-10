#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
import sys
from getkey import getkey, keys
from std_srvs.srv import Empty


def turtle_talker():
    #*****************set up lines*************
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtle_control', anonymous=True)
    rate = rospy.Rate(1)#1Hz
    msg = Twist()
    reset = rospy.ServiceProxy('reset', Empty)
    #*******************************************

    #the variables to assign values to for linear and angular velocity
    lv = 0#default values so if you try and run this code unedited it will work and the turtle won't move
    av = 0

    # this resets the turtle and clears the path, not needed here but you will need it for an exercise
    reset()

    while not rospy.is_shutdown():#everything in this code block happens repeatedly at the rate set above

        # put your code here

        #**************** Send the commands to the robot*****************
        msg.angular.z = float(av)
        msg.linear.x = float(lv)
        pub.publish(msg)#send values
        rate.sleep()#add a pause so the block repeats at the right frequency
        #****************************************************************

if __name__ == '__main__':
    try:
        turtle_talker()
    except rospy.ROSInterruptException:
        pass