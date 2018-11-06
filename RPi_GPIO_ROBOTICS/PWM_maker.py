import RPi.GPIO as gp

gp.setmode(gp.BOARD)

# use pin number 11 for LED
led = 11

# set pin as output
gp.setup(led,gp.OUT)

# set pwm frequency
frequency = 100

# initial PWM
my_pwm = gp.PWM(led,frequency)

# PWM starting
my_pwm.start(50)

duty = 50 

for i in range(10):

	duty = input("dutyCycle:")

	my_pwm.ChangeDutyCycle(duty)

	frequency = input("frequ :")

	my_pwm.ChangeFrequency(frequency)

my_pwm.stop()

gp.cleanup()
