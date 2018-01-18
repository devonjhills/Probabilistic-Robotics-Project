#!/usr/bin/env python

# Based off of learnturtlebot tutorials

import rospy
import yaml
from my_move_base import MyMoveBasePath

if __name__ == '__main__':

    # saved gmap data
    with open("route.yaml", 'r') as stream:
        dataMap = yaml.load(stream)

    try:
        rospy.init_node('my_movebase', anonymous=False)
        navigator = MyMoveBasePath()

        for obj in dataMap:

            if rospy.is_shutdown():
                break

            name = obj['filename']

            rospy.loginfo("Go to %s pose", name[:-4])
            success = navigator.goto(obj['position'], obj['quaternion'])
            if not success:
                rospy.loginfo("Failed to reach %s pose", name[:-4])
                continue
            rospy.loginfo("Reached %s pose", name[:-4])

            rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Quitting")
