import RPi.GPIO as gpio

# to use board physical numbers 
# for gpio should use BCM insted of BOARD
gpio.setmode(gpio.BOARD)

# set a pin as output 

gpio.setup(11,gpio.OUT)
mode = (input("1 for T/0 for F\n"))
gpio.output(11,mode)

gpio.cleanup()
