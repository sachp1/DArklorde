import cv2    
import numpy as np
def mapp(le):
	im=cv2.imread(le) # read picture
	cv2.imshow("letter",im)
	#white=cv2.imread('white.jpg')
	imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # BGR to grayscale   Contour 1 Top Left
	ret,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY_INV)
	arr=np.array([[[0,0],[0,166],[0,322]],[[166,0],[166,166],[166,322]],[[322,0],[322,166],[322,322]]]) #numpy array for getting the cooordinates
	for i in xrange(3):
		for j in xrange(3):
			a=arr[i][j][0]
			b=arr[i][j][1]
			newimg=thresh[a:166+a,b:166+b]
			countours,hierarchy=cv2.findContours(newimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(im[a:a+166,b:b+166],countours,-1,(0,255,0),3)
			print(hierarchy)
			cv2.waitKey(0)
			cnt=countours[0]
			M = cv2.moments(cnt)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			cv2.circle(im,(cx+b,cy+a),10,(255,255,0),-1) 
			j=j+167
		i=i+167
	cv2.imshow("Contour",im)	
	cv2.waitKey(0)
	cv2.destroyAllWindows()









