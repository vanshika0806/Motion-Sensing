import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"]) #we create a pandas dataframe with 2 columns start and end

video=cv2.VideoCapture(0)

while True:
    check, frame=video.read() #first gets the first frame of the video and then rest of the frames
    status=0 #when there is no object in the first frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #frame will be converted into gray frame
    gray=cv2.GaussianBlur(gray,(21,21),0) #blur the image make it smooth as it removes noise and increases accuracy in the calculation

    if first_frame is None: #true in the first iteration of the loop
        first_frame=gray  #so assign the grayscale image of the first frame
        continue

    delta_frame=cv2.absdiff(first_frame,gray)   #compares the first background frame and current frame 

    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]  #set the threshold image and value, it returns a tuple with 2 value
    #for threshold binary we need to access only the second item of the tuple which is the actual frame that is returned from the threshold tuple

    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2) #smoothen or dilate the threshold image, more the iterations smoother the image

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#find all the contours of the distinct objects in the dilated threshold frame
    #we need to find the contours and check their areas so we store them in a tuple cnts
    #we use a copy of the thresh frame so we dont modify the original frame

    for contour in cnts:  #we filter out the contours as we only want those with area>1000 pixels
        if cv2.contourArea(contour)<1000:
            continue 
        status=1 #when countour area >1000 ie when a moving object is present    

        (x,y,w,h)=cv2.boundingRect(contour)  #for countour area>1000 we draw a rectangle around that object
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        
    status_list.append(status)

    if status_list[-1]==1 and status_list[-2]==0:  #if the last item is 1 and second last is 0 that means object has left the frame
        times.append(datetime.now())  #record the timestamp
    if status_list[-1]==0 and status_list[-2]==1:  #if 0 then 1 means object has entered the frame
        times.append(datetime.now())


    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame) #shows the image after comparing ie the difference
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)


    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame) #gives the difference bw the intensities of the corressponding pixels
    #higher the difference means motion, less diff means no motion

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)  #we get the actual status of each frame 0 for no object 1 for moving object
print(times) 

for i in range(0,len(times),2):  #iterating through the timestamps list from 0 to the length of the list with a period of 2 and append those values into the dataframe
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows

#store the current frame so the as soon as the video starts we want to store the numpy area in a variable and make it statis so that its value doesnt change while the 'while' loop runs in the script

#we store the timestamps list into a Pandas dataframe and then into a csv file
#statr column will have the entry values and end column will have the exit values