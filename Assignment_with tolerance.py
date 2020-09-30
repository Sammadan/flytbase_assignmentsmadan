import time
from flyt_python import api

drone = api.navigation()  

time.sleep(3)

print ('drone is taking off now')
drone.take_off(5.1)

print("Move in square with side of  6.5 at the height of 5m ")
drone.position_set(6.5, 0, 0,relative=True, body_frame=True)
drone.position_set(1.2, 6.5, 0,relative=True, body_frame=True)
drone.position_set(-6.5,1.22, 0,relative=True, body_frame=True)
drone.position_set(-1.25, -6.5, 0,relative=True, body_frame=True)

print ('drone is Landing now')
drone.land(async=True)

drone.disconnect()
