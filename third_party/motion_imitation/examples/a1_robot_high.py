"""Apply the same action to the simulated and real A1 robot.


As a basic debug tool, this script allows you to execute the same action
(which you choose from the pybullet GUI) on the simulation and real robot
simultaneouly. Make sure to put the real robbot on rack before testing.
"""
import time
import numpy as np
from robot_interface_high import RobotInterface # pytype: disable=import-error

max_mag = 0.3

i = RobotInterface()
for _ in range(300):
    o = i.receive_observation()
    highcmd = np.zeros(8, dtype=np.float32)
    highcmd[0] = 2.0 #  mode            // 1 - standing // 2 - walking
    highcmd[1] = 0.0 # cmd.forwardSpeed = highcmd[1];  //  forwardSpeed    [-1,1] = [-0.5,0.8]m/s
    highcmd[2] = -1.0 # cmd.sideSpeed = highcmd[2];     //  sideSpeed       [-1,1] = [-0.3,0.3]m/s
    highcmd[3] = 0.0 # cmd.rotateSpeed = highcmd[3];   //  rotateSpeed     [-1,1] = [-50,50]degrees/s
    highcmd[4] = 0.0 # cmd.bodyHeight = highcmd[4];    //  bodyHeight      [-1,1] = [0.3,-0.45]m
    highcmd[5] = 0.0 # cmd.roll = highcmd[5];          //  roll            [-1,1] = [-20,20]degrees
    highcmd[6] = 0.0 # cmd.pitch = highcmd[6];         //  pitch           [-1,1] = [-20,20]degrees
    highcmd[7] = 0.0 # cmd.yaw = highcmd[7];           //  yaw             [-1,1] = [-28,28]degrees

    highcmd[1:] = np.clip(highcmd[1:],-max_mag,max_mag)
    i.send_command(highcmd)
    time.sleep(0.01)

