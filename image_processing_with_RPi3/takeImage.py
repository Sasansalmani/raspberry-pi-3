import time 
import picamera as pc 
import picamera.array 
import cv2 
import numpy as np 


class Image():
	def __init__(self,img):
		self.image = img[:,:]
	def ret_image(self):
		return self.image

def show_image():
	global cap
	# define camera frame size
	image = picamera.array.PiRGBArray(cap, size=(640,480)) 
	i = 0
	for frame in cap.capture_continuous(image, format="bgr", use_video_port=True):
		# change to array for use as an image
		img = frame.array
		# define object from "Image" class
		shape=Image(img)
		cv2.imshow("Frame", shape.ret_image())
		key = cv2.waitKey(1) & 0xFF 
		if key == ord('t'):
			str = "image%d.jpg"%i
			cv2.imwrite(str,img)
			i = i+1
			print("taken")
			print(i-1)
		# make memory free for re_load image 
		image.truncate(0)
		if key == ord("q"):
			cv2.destroyAllWindows()
			break


def main():
	# call function for start taking image
	show_image()

cap = pc.PiCamera()
# set resolution for camera 
cap.resolution=(640,480) 
# set frame rate for camera 
cap.framerate=30 
print("for exit press 'q'") 
print("for take image press 't'") 
main()
