import time
from flyt_python import api

drone = api.navigation()  

time.sleep(3)

print ('drone is taking off now')
drone.take_off(5.0)

print("Move in square with side of  6.5 at the height of 5m ")
drone.position_set(6.5, 0, -5, relative=False)
drone.position_set(6.5, 6.5, -5, relative=False)
drone.position_set(0, 6.5, -5, relative=False)
drone.position_set(0, 0, -5, relative=False)

print ('drone is Landing now')
drone.land(async=False)
drone.disconnect()


