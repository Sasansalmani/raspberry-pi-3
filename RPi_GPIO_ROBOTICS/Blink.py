import RPi.GPIO as gp
import time

green = 11

gp.setmode(gp.BOARD)
gp.setup(green,gp.OUT)

gp.output(green,1)
time.sleep(1)

gp.output(green,0)
time.sleep(1)

gp.cleanup()
