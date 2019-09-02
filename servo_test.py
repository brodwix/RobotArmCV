import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

# angle to PWM duty cycle
# 0 degrees = 2.5
# 90 degrees = 7.5
# 180 degrees = 12.5

def get_pwm(angle):
    return(angle/18.0)+2.5

angle_control = [0,45,90,135,180]

p.start(get_pwm(0)) # Initialization

try:
       while True:
           for x in range(5):
             print(angle_control[x])
             p.ChangeDutyCycle(get_pwm(angle_control[x]))
             time.sleep(0.5)
             
           
           for x in range(3,0,-1):
             print(angle_control[x])
             p.ChangeDutyCycle(get_pwm(angle_control[x]))
             time.sleep(0.5)
           
except KeyboardInterrupt:
    GPIO.cleanup()
