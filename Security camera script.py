import cv2
import winsound

def main():
    cam = cv2.VideoCapture(0)
    while 1:
        ret, frame1 = cam.read()
        ret, frame2 = cam.read()
        diff= cv2.absdiff(frame1,frame2)
        gray= cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur= cv2.GaussianBlur(gray, (5,5), 0)
        _, thres= cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilate = cv2.dilate(thres, None, iterations=3)
        contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i in contours:
            if cv2.contourArea(i) < 5000:
                continue
            x, y, w, h= cv2.boundingRect(i)
            cv2.rectangle(frame1, (x,y), (x+w,y+h), (255,128,0))
            winsound.Beep(800,20)
        cv2.imshow('Security Camera', frame1)
        k= cv2.waitKey(1)
        if k == 27 or k==13:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
