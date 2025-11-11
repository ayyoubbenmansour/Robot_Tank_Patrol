# servo_control.py
import pigpio
import time

pi = pigpio.pi()

PAN_PIN = 13
TILT_PIN = 12

# Servo angle limits
MIN_ANGLE = 0
MAX_ANGLE = 180

# Current angles (start centered)
current_pan = 90
current_tilt = 90

def angle_to_pulse(angle):
    return int(500 + (angle / 180.0) * 2000)  

def set_pan(angle):
    global current_pan
    angle = max(MIN_ANGLE, min(MAX_ANGLE, angle))
    current_pan = angle
    pi.set_servo_pulsewidth(PAN_PIN, angle_to_pulse(angle))

def set_tilt(angle):
    global current_tilt
    angle = max(MIN_ANGLE, min(MAX_ANGLE, angle))
    current_tilt = angle
    pi.set_servo_pulsewidth(TILT_PIN, angle_to_pulse(angle))

# Movement functions
def pan_right(): set_pan(current_pan - 5)
def pan_left(): set_pan(current_pan + 5)
def tilt_up(): set_tilt(current_tilt - 5)
def tilt_down(): set_tilt(current_tilt + 5)
def center(): set_pan(90), set_tilt(90)

def get_angles():
    return current_pan, current_tilt

