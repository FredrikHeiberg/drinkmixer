from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

print "FILE RUN"

mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(3)

myMotor.setSpeed(255)

def mixDrink():
	myMotor.run(Adafruit_MotorHAT.RELEASE);

	myMotor.run(Adafruit_MotorHAT.FORWARD)
	time.sleep(5.0)

mixDrink()