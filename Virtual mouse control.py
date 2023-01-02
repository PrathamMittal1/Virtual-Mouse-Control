import cv2
import mediapipe as mp
import pyautogui

print('''Virtual mouse control
version=1, created by: PRATHAM MITTAL, email: pratham9897521595@gmail.com
Use your index and middle finger to control the cursor. 
Bend your index finger and middle finger for 
left click and right click functions respectively.''')
cap = cv2.VideoCapture(0)                           #camera on
hands_detector = mp.solutions.hands.Hands()         #hand detector
drawing = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_x, index_y, middle_x, middle_y = 0, 0, 0, 0   #variables
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, ch = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)
                screen_ratio = (screen_width / frame_width, screen_height / frame_height)
                if id == 8:                         # index finger tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), 2)
                    index_x, index_y = screen_ratio[0] * x, screen_ratio[1] * y
                if id == 12:                        # middle finger tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), 2)
                    middle_x, middle_y = screen_ratio[0] * x, screen_ratio[1] * y
                if id == 5:                         # index finger mid
                    cx, cy = screen_ratio[0] * x, screen_ratio[1] * y
                    pyautogui.moveTo(cx, cy)
                    if abs(cy - index_y) < 20:
                        print('left click')
                        pyautogui.leftClick()
                        pyautogui.sleep(1)
                if id == 9:                         # middle finger mid
                    cx, cy = screen_ratio[0] * x, screen_ratio[1] * y
                    if abs(cy - middle_y) < 20:
                        pyautogui.rightClick()
                        print('right click')
                        pyautogui.sleep(1)

    cv2.imshow('Virtual mouse control', frame)
    k = cv2.waitKey(1)
    if k == 27 or k == 13:
        break
cv2.destroyAllWindows()
