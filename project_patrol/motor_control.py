import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Motor Pins (L298N)
ENA = 22
IN1 = 18
IN2 = 16

ENB = 11
IN3 = 15
IN4 = 12

# Setup pins
for p in [ENA, IN1, IN2, ENB, IN3, IN4]:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, False)

# Enable motors
GPIO.output(ENA, True)
GPIO.output(ENB, True)

def forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def stop():
    for p in [IN1, IN2, IN3, IN4]:
        GPIO.output(p, False)

