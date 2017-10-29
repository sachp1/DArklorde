import cv2
#import letter
import numpy as np
def mapp(x1):
	oo=ord(x1)
	str1=oo-97
	le=str(str1)+".jpg"
	im=cv2.imread(le) # read picture
	#cv2.imshow("word",im)
	white=cv2.imread("white.jpg")
	imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # BGR to grayscale   Contour 1 Top Left
	ret,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY_INV)
	#arr=np.array([[[0,0],[0,166],[0,322]],[[166,0],[166,166],[166,322]],[[322,0],[322,166],[322,322]]]) #numpy array for getting the cooordinates
	countours1,hierarchy1=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt1=countours1[0]
	x,y,w,h = cv2.boundingRect(cnt1)
	x3=w/3
	y3=h/3
	x-=20
	y-=20
	w+=40
	h+=40
	for i in range(x,w,x3):
		for j in range(y,h,y3):
#			a=arr[i][j][0]
#			b=arr[i][j][1]
			a=i
			b=j
			newimg=thresh[a:x3+a,b:y3+b]
			countours,hierarchy=cv2.findContours(newimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(im[a:a+x3,b:b+y3],countours,-1,(0,255,0),2)
			print(hierarchy)
			cv2.waitKey(0)
			if(countours):
				cnt=countours[0]
				M = cv2.moments(cnt)
				if(M['m00']==0):	
					break
				cx = int(M['m10']/M['m00'])
				cy = int(M['m01']/M['m00'])
				#if np.any(thresh[cx+b,cy+a]==255):
				cv2.circle(im,(cx+b,cy+a),10,(255,20,10),-1)
			#j=j+167
		#i=i+167
	cv2.imshow("Contour",im)	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

word=input("\nInput a word : ")
l=len(word)
for i in range(0,l):
	if(word[i].isalpha()):
 		mapp(word[i]) 