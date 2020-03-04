from roboclaw import Roboclaw
import time

roboclaw = Roboclaw("/dev/ttyACM0", 115200)

print(roboclaw.Open())

address = 0x80
roboclaw.ResetEncoders(address)

# while 1:
# 	#Get version string
# 	version = roboclaw.ReadVersion(0x80)
# 	if version[0]==False:
# 		print "GETVERSION Failed"
# 	else:
# 		print repr(version[1])
# 	time.sleep(1)

print roboclaw.ReadEncM1(address)[1]

roboclaw.ForwardM1(address, 40)
roboclaw.ForwardM2(address, 40)

time.sleep(3)

roboclaw.ForwardM1(address, 0)
roboclaw.ForwardM2(address, 0)

print roboclaw.ReadEncM1(address)[1]

