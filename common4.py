from brian2 import *
from time import time
import parameters3 as par
import numpy as np
import pandas as pd
#import cv2
from PIL import Image, ImageDraw


def read_img():
        

	#img = cv2.imread("4*4(1).png", 0)
	#img2 = cv2.imread("4*4(2).png",0)

	#img = np.ndarray.flatten(img)
	#img2 = np.ndarray.flatten(img2)

	#return img
        pass

#запись веосов
def recon_weights(W, dt):

	for i in range(par.hid_size):
		temp = W[i]
		recon = np.reshape(temp,(3,3))

		name  = f"/Users/tortolla/Desktop/2024/zazzaa" + str(dt) + "(" + str(i) + ")" ".png"


		with open(name, 'w') as file:
        		file.write(str(recon))

		recon = recon*255
		#recon = np.reshape(temp, (3, 3)) * 255

		image = Image.new("L", (3, 3))

		for i in range(0, 3):
			for j in range(0, 3):
				color = int(recon[i][j])
				draw = ImageDraw.Draw(image)
				draw.point((i, j), fill=(int(recon[i][j])))

		image.save(name)

		#image = Image.fromarray(recon)
		#name = f"{dt}.png"

		#image.save(name)

		

def image(W, dt):
	temp = W
	recon = np.reshape(temp,(3,3))*255

	image = Image.fromarray(recon)
	name = f"{dt}.png"
	image.save(name)



   
	
