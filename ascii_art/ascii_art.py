from PIL import Image
import numpy as np

symList = ('#','8','X','H','0','T','I','L',')','i','=','+',';',':',',','.',' ')

imgFile = Image.open('D:/imgIn.png')
imgSize = imgFile.size
imgWid = imgSize[0]
imgHgt = imgSize[1]
imgRaw = np.asarray(imgFile.convert('L')).astype('float')
imgSym = [i/16 for i in imgRaw]
imgSym = np.array(np.round(imgSym)).astype('int')

imgOut = open('D:/imgOut.txt','w+')
for i in range(imgHgt):
	for j in range(imgWid):
		imgOut.write(symList[int(imgSym[i][j])])
	imgOut.write('\n')

imgOut.close()
