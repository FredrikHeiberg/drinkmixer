from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit


mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(3)

def mixTheDrink(name, size):
	time = 5.0

	myMotor.setSpeed(255)
	myMotor.run(Adafruit_MotorHAT.RELEASE);
	myMotor.run(Adafruit_MotorHAT.FORWARD)

	percentage(time)
	time.sleep(time)
	
	turnOffMotors()

def romAndCoke():
	print "test"

def ginAndTonic():
	print "test1"

def fantaAndVodka():
	print "test3"

def percentage(time):
	for i in range(1,time):
		i = i + 1
		time.sleep(1.0)