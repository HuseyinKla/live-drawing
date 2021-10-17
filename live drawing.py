import cv2 as cv
import math


def islemler(event,x,y,flags,params):

    global centerx,centery,isCenter,hold,rad,tempy,tempx,pt1,pt2,ispt1,ispt2,holdrec
    tempx=x
    tempy=y
    pt2=(x,y)
    #print("X ekseni->"+str(x)+"Y ekseni ->"+str(y))
    if event == cv.EVENT_LBUTTONDOWN:
        centerx=x
        centery=y
        isCenter=True
        hold=True

    if event == cv.EVENT_LBUTTONUP:
        #çizilen şeyin kalıcı olması için aç
        if event==cv.EVENT_LBUTTONDOWN:
            hold=False

    if event==cv.EVENT_RBUTTONDOWN:
        pt1=(x,y)
        ispt1=True
        holdrec=True

    if event==cv.EVENT_RBUTTONUP:
        #çizilen şeyin kalıcı olması için aç
        if event==cv.EVENT_RBUTTONDOWN:
            holdrec=False

holdrec=False
centerx=0
centery=0
tempx=0
tempy=0
isCenter=False
hold=False
rad=0
pt1=(0,0)
pt2=(0,0)
ispt1=False
ispt2=False

cv.namedWindow("pencere")
vid = cv.VideoCapture(0)
cv.setMouseCallback("pencere",islemler)

while 1:
    r,frame = vid.read()


    if isCenter:
        cv.circle(frame,(centerx,centery),3,(0,0,255),-2)
    if hold:
        cv.circle(frame,(centerx,centery),int((math.sqrt((centerx-tempx)**2+(centery-tempy)**2))),(0,0,255),5)

    if ispt1:
        cv.circle(frame,pt1,4,(0,0,255),-2)
    if holdrec:
        cv.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv.imshow("pencere",frame)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break

vid.release()
cv.destroyAllWindows()