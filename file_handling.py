import cv2
import time
key = cv2. waitKey(100)
webcam = cv2.VideoCapture(0+ cv2.CAP_DSHOW)
webcam.set(3, 640)
webcam.set(4, 480)
#http://discuss.codingblocks.com/t/error-while-using-webcam/44932/6
#time.sleep(1.00) #+ cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
#webcam.set(cv2.CAP_PROP_FOURCC, 0x32595559)
#webcam.set(cv2.CAP_PROP_FPS, 25)
#check, frame = webcam.read()
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(100)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

img = cv2.imread("saved_img.jpg")
height, width, _ = img.shape
cv2.waitKey(0)
cv2.destroyAllWindows()