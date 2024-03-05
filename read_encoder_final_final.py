#!/usr/bin/env python3
import rospy
import serial
from time import sleep
from std_msgs.msg import Int32,Float32,String
from geometry_msgs.msg import Twist

SCALE_FACTOR_VEL_LEFT =  3.14159*0.65
SCALE_FACTOR_VEL_RIGHT =  3.14159*0.65
# rosrun rqt_plot rqt_plot
L = 0.195 #scale khoang cach 2 banh xe la 19.5cm
D = 0.65 #duong kinh banh xe la 65mm
PHI = L*0.5
SCALE_FACTOR_ANG_LEFT  =  100
SCALE_FACTOR_ANG_RIGHT  = 100
tx_buffer = '+00.00/+00.00/y/n'
linear_x = 0.0
angular_z = 0.0
v_L = 0.0
v_R = 0.0
encoder_left = 0
encoder_right = 0
vel_pub_msg = Twist()
setpoint_left = 0
setpoint_right = 0
vel_left = 0 #toc do encoder banh trai sau khi lam tron
vel_right = 0
def MOTOR_Enc_Cal():
    global encoder_left, encoder_right, linear_x, angular_z
    v_L = linear_x - angular_z * PHI
    v_R = linear_x + angular_z * PHI
    encoder_left = v_L/SCALE_FACTOR_VEL_LEFT 
    encoder_right = v_R/SCALE_FACTOR_VEL_RIGHT
    print(encoder_left)
    print(encoder_right)
def MOBILE_Vel_Cal():
    global v_L, v_R, encoder_left, encoder_right
    global vel_pub_msg
    v_L = SCALE_FACTOR_VEL_LEFT*encoder_left 
    v_R = SCALE_FACTOR_VEL_RIGHT*encoder_right
    vel_pub_msg.linear.x = (v_L + v_R)/2.0
    vel_pub_msg.angular.z = (v_R - v_L)/L
def Callback1(value):
    global setpoint_left,vel_left,vel_right
    global setpoint_right
    ser = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1)
    tx_buffer = '+00.00/+00.00/y/n'
    # if value.angular.z == 0:
    #     val_encod_left = value.linear.x*SCALE_FACTOR_VEL_LEFT
    #     val_encod_right = value.linear.x*SCALE_FACTOR_VEL_RIGHT
    # else:
    #     if value.angular.z > 0:
    #         val_encod_left = 0 #-value.angular.z*SCALE_FACTOR_ANG_LEFT
    #         val_encod_right = value.angular.z*SCALE_FACTOR_ANG_RIGHT
    #     else:
    #         val_encod_left = value.angular.z*SCALE_FACTOR_ANG_LEFT
    #         val_encod_right = 0 #value.angular.z*SCALE_FACTOR_ANG_RIGHT
	MOTOR_Enc_Cal()
    vel_left = round(encoder_left)
    vel_right = round(encoder_right)
    #rospy.loginfo("OK")
    
    if vel_left and vel_right > 0:
        tx_buffer = '+' + str(vel_left) +'.00/+' + str(vel_right) + '.00/y/n'
        rospy.loginfo("Forward")
    elif vel_left == 0 and vel_right > 0:
    	tx_buffer = '+00.00/+' + str(vel_right) + '.00/y/n'
    	rospy.loginfo("Turn Left")
    elif vel_left > 0 and vel_right == 0:
    	tx_buffer = '+'+str(vel_left) +'.00/+00.00/y/n'
    	rospy.loginfo("Turn Right")
    elif vel_left < 0 and vel_right < 0:
    	tx_buffer = str(vel_left) +'.00/' + str(vel_right) + '.00/y/n'
    	rospy.loginfo("Backward")
    ser.write(tx_buffer.encode())
    rospy.logwarn(tx_buffer)
def main(): 
    setpoint = Twist()
    encoder1_left = Float32()
    encoder2_right = Float32()	
    ser = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1) 
    rospy.init_node('read_encoder', anonymous=True)
    rat = rospy.Rate(100)
    encoder1_left_pub = rospy.Publisher('/encod1_left_val', Float32, queue_size=10)
    encoder2_right_pub = rospy.Publisher('/encod2_right_val', Float32, queue_size=10)
    setpoint_ = rospy.Publisher('/setpoint12', Twist, queue_size=10)
    vel_pub = rospy.Publisher('vel_pub', Twist, queue_size=10)
    rospy.Subscriber('/cmd_vel',Twist, Callback1)
    encoder = Float32()
    while not rospy.is_shutdown():
    	try:
	    	while True:
	    		encoder_rx = ser.readline().decode('utf-8')
	    		ser.flush()
	    		encoder1_left_temp = encoder_rx[:7]
	    		encoder2_right_temp = encoder_rx[8:15]
	    		setpoint1_temp = encoder_rx[15:18]
	    		setpoint2_temp = encoder_rx[19:22]
	    		if setpoint1_temp[0] == '+':
	    			setpoint.linear.x = float(setpoint1_temp[1:])
	    		elif setpoint1_temp[0] == '-':
	    			setpoint.linear.x = -float(setpoint1_temp[1:])
	    		if setpoint2_temp[0] == '+':
	    			setpoint.linear.y = float(setpoint2_temp[1:])
	    		elif setpoint2_temp[0] == '-':
	    			setpoint.linear.y = -float(setpoint2_temp[1:])
	    		if encoder1_left_temp[0] == '+':
	    			encoder1_left = float(encoder1_left_temp[2:7])
	    		elif encoder1_left_temp[0] == '-':
	    			encoder1_left = -float(encoder1_left_temp[2:7])
	    		else:
	    			rospy.logwarn("OKOK")
	    		if encoder2_right_temp[0] == '+':
	    			encoder2_right = float(encoder2_right_temp[2:7])
	    		elif encoder2_right_temp[0] == '-':
	    			encoder2_right = -float(encoder2_right_temp[2:7])
	    		rospy.loginfo(encoder_rx)
	    		rospy.logwarn(encoder1_left_temp)
	    		rospy.loginfo("------")
	    		rospy.logwarn(encoder2_right_temp)
	    		rospy.loginfo("*******")
	    		rospy.logwarn(setpoint)
	    		setpoint_.publish(setpoint)
	    		encoder1_left_pub.publish(encoder1_left)
	    		encoder2_right_pub.publish(encoder2_right)
				MOBILE_Vel_Cal()
				vel_pub.publish(vel_pub_msg)
    	except KeyboardInterrupt:
    		ser.close()
    		break
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
