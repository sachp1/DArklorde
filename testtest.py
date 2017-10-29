import cv2
import numpy
le=".jpg"
nmm=input("enter letter")
my1=ord(nmm)-97
lle=str(my1)+le
im=cv2.imread(lle) # read picture
#cv2.imshow("word",im)
white=cv2.imread("white.jpg")
imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # BGR to grayscale   Contour 1 Top Left
ret,thresh=cv2.threshold(imgray,200,255,cv2.THRESH_BINARY_INV)
#arr=np.array([[[0,0],[0,166],[0,322]],[[166,0],[166,166],[166,322]],[[322,0],[322,166],[322,322]]]) #numpy array for getting the cooordinates
countours1,hierarchy1=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt1=countours1[0]
x,y,w,h = cv2.boundingRect(cnt1)
x-=8
y-=8
w+=16
h+=16
cv2.circle(im,(x,y),10,(255,20,10),-1)
x3=float(w/3)-10
y3=float(h/3)-10
print"width",w
print"\n height",h
print"\n w/3",x3
print"\n h/3",y3
cv2.rectangle(im,(x,y),(x+w,y+h),(200,30,30),5)
cv2.imshow("wow",im)
cv2.waitKey(0)
pi=y+h
hi=h/3
wi=w/3
for i in range(y,h,hi+10):
		for j in range(x,w,wi+10):
			newimg=thresh[j:x3+j,i:y3+i]
			countours,hierarc16y=cv2.findContours(newimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(im[j:j+x3,i:i+y3],countours,-1,(10,255,10),2)
			if(countours):
				cnt=countours[0]
				M = cv2.moments(cnt)
				if(M['m00']==0):	
					break
				cx = int(M['m10']/M['m00'])
				cy = int(M['m01']/M['m00'])
				#if np.any(thresh[cx+b,cy+a]==255):
				cv2.circle(im,(cx+i,cy+j),10,(255,20,10),-1)

			
cv2.imshow("img mod",im)
cv2.waitKey(0)
cv2.destroyAllWindows()