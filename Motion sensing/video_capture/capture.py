import cv2, time 

video = cv2.VideoCapture(0,cv2.CAP_DSHOW) #create an object video to trigger a video capture object with an argument as video file path or 0,1,2,3 index for webcam depending on which camera youre using
#the above statement triggers the webcam for a sec the one below releases it immediately

a=0

while True:
    a=a+1 #to display no of frames approx 20 frames per sec
    check, frame=video.read()
    print(check)  #boolean value, we get true
    print(frame)  #numpy array 3dimen as coloured has matrices of each image captured in the video

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converts a coloured frame to a gray image
    #ime.sleep(3) #holds it for 3 secs
    cv2.imshow("Capturing",gray) #shows a window "capturing" passing the frame object
    #numpy array is displayed after every iteration
    key=cv2.waitKey(1) #frame changes after every 1 mili secs

    if key==ord('q'): #if you press q key, breaks the while loop and video will stop window will be destroyed 
        break
print(a)
video.release() #access your object and release the camera ie close it
cv2.destroyAllWindows
