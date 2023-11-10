#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
import sys
from getkey import getkey, keys
from std_srvs.srv import Empty
from data_package.datarecording import playback

# def playback(instructions, rec_mode, play_mode):
#     if instructions:
#         print(len(instructions))
#         if play_mode:
#             instruction = instructions.pop(0)
#             lv = instruction['lv']
#             av = instruction['av']
#         else:
#             instruction = instructions.pop()  # 0)
#             lv = -instruction['lv']
#             av = -instruction['av']
#     else:
#         lv = 0
#         av = 0
#         rec_mode = True
#
#     return lv, av, rec_mode

def turtle_talker(lv,av):
#def turtle_talker():#switch to this function def to remove commandline arguments
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

        #lv, av = map(float, raw_input('enter velocity values: ').split())

        if rec_mode:
            key = getkey()
            if key == keys.UP:
                lv += 0.1
            elif key == keys.DOWN:
                lv -= 0.1
            elif key == keys.LEFT:
                av -= 0.1
            elif key == keys.RIGHT:
                av += 0.1
            elif key == 'r':
                #rospy.wait_for_service('reset', Empty)
                reset()
            elif key =='p':
                reset()
                rec_mode = False
                play_mode = True
            elif key == 'b':
                rec_mode = False
                play_mode = False
            else:
                 print("X")

            if key != 'r' and key != 'p' and key != 'b':
                instructions.append({'lv':lv, 'av':av})

        else:
            lv, av, rec_mode = playback(instructions, rec_mode, play_mode)


        msg.angular.z = float(av)
        msg.linear.x = float(lv)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        turtle_talker(sys.argv[1], sys.argv[2])
        # turtle_talker()#switch to this function call to remove commandline arguments
    except rospy.ROSInterruptException:
        pass