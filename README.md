# Virtual-Mouse-Control
Artificial Virtual Mouse Pointer Controller via hand fist and computer vision.


This project requires a lot of hand exercise as we’ll control the mouse cursor of our computer with our hand, or I should say with just only two fingers.
Three modules are imported in the script, viz. cv2, mediapipe and pyautogui.
OpenCV for image/video processing, mediapipe for hand landmarks, and pyautogui for mouse and screen methods.

Firstly, we turn on camera, initializes hands detector and drawing utils, extracts the screen’s shape, and initializing some variables.
Then we start a while loop to capture the video. Flipping the frame is necessary because generally video from a front camera sensor is not laterally inverted. Then we extract the frame’s shape and detects the hands using the hand detector that we initialized earlier. If there are hands, we draw the landmarks for each of the detected hands and if the landmark is for index or middle finger’s tip, we draw a circle around it.
Secondly, if we found that the distance between the tip of index finger and its mid joint is less than 20px then left click of the cursor is called. Similarly, if we found that the distance between the tip of middle finger and its middle joint is less than 20px then right click of the cursor is called.
Then finally, I’ve added functionality to exit the infinite loop by pressing Esc or Enter key.
