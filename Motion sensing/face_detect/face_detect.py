import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #reading the cascade by creating a cascade classifier object
img=cv2.imread("news.jpg") 

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts coloured image to greyscale
#gives the pixel(upper left corner) from where face starts and the length and width 
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,   #detecting faces of various sizes for accuracy choose low value
minNeighbors=5) 

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #drawing the rect around the face(image,coordinates of top left and bottom right corner,color of the rectangle,width of the rect)

print(type(faces))  #gives a numpy array with 4 values
print(faces)  #[155 83 382 382] 155th colum 83rd row, width 382 and height 382

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()