from time import sleep
import RPi.GPIO as gp

gp.setmode(gp.BCM)
but1 = 18
but2 = 16
gp.setup(but1,gp.IN,pull_up_down=gp.PUD_UP)
gp.setup(but2,gp.IN,pull_up_down=gp.PUD_UP)
led = 21
gp.setup(led,gp.OUT)
while (1):
	if gp.input(but1)==0 and gp.input(but2)==0:
		break
	elif gp.input(but1)==0:
		gp.output(led,True)
	elif gp.input(but2)==0:
		gp.output(led,False)
gp.cleanup()
print ("finish")

