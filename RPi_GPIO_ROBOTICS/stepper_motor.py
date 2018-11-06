import RPi.GPIO as gp
import time

gp.setmode(gp.BOARD)

# two pin for stepper motor driver
step = 40
dire = 38

gp.setup(step,gp.OUT)
gp.setup(dire,gp.OUT)

frequency = 40

my_pwm = gp.PWM(step,frequency)


def SpinMotor(dir,num_steps):
	gp.output(dire,dir)
	while num_steps > 0:
		my_pwm.start(1)
		time.sleep(0.1)
		num_steps -= 1
	my_pwm.stop()


di = raw_input("direction c or u ")
num = input("numbers")
if di == 'c':
	SpinMotor(False, num)
else:
	SpinMotor(True, num)

gp.cleanup()
