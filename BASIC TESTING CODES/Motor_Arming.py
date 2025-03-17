from pymavlink import mavutil
import time

# Connect to the Cube+ autopilot via MAVProxy
master = mavutil.mavlink_connection("/dev/ttyUSB0", baud=57600)

# Wait for a heartbeat before sending commands
print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Heartbeat received! Vehicle detected.")

# Ensure RC3 (Throttle) is at minimum before arming
THROTTLE_MIN = 1100  # Adjust if necessary (1100 is safe)
master.mav.rc_channels_override_send(
    master.target_system, master.target_component,
    0, 0,1100, 0, 0, 0, 0, 0
)
time.sleep(1)  # Wait a moment

# Send arm command
print("Arming motors...")
master.arducopter_arm()
master.motors_armed_wait()
print("Motors armed successfully!")
# Keep script running to maintain connection
while True:
    time.sleep(1)