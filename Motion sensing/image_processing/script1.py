import cv2

img=cv2.imread("galaxy.jpg",0) #imread(path of the image to load,-1 or 0 oe 1)
                               #-1 for transparency in image, 0 fo r b&w and 1 for coloured image with 3 bands
print(type(img)) #prints a numpy n dimensional matrix each no. being each pixel of the image
print(img) #python stores the image as a matrix of no.s ie the numpy array
print(img.shape) #prints image resolution ie the size of the numpy matrix
print(img.ndim) #prints no of dimensions of the image b&w then 2, coloured then 3 as red,green,blue 3 bands

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resizes the image or the numpy array to the given values
cv2.imshow("Galaxy",resized_image) #to display a window "Galaxy" that displays the image
cv2.imwrite("Galaxy_resized.jpg",resized_image) #stores the resized image in a new file
cv2.waitKey(2000) #if value is 0 the window will close when you press any key, if 2000 ie 2 secs then it closes after 2 sec
cv2.destroyAllWindows() #specifies what happens after 2 secs or after user presses any button
