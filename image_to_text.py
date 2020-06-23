import cv2
import numpy as np
import requests
import io
import json
import pyttsx3
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0) #+ cv2.CAP_DSHOW)
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
        key = cv2.waitKey(10)
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

# Cutting image
# roi = img[0: height, 400: width]
roi = img

# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "1e97cc8a8888957",
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()
speak(text_detected)
print(type(text_detected))
text_detected1=text_detected
print("want to create the text file or want to listin alread created files")
r=int(input("press 1 for lishen alread created files 2 :"))
def this():
	with open("this.txt","r") as f:
		data=f.readlines()	
	f.close()
	return data
if r==1:
	data=this()
	print(data)
	data=data[0]
	print(data)
	data=int(data)
	data=data+1
	data=str(data)
	print(data)
	a1=open("this.txt",'w')
	a1.write(data)
	a1.close()
	a=open(data,'w')
	a.write(text_detected1)
	a.close()
r1=int(input("want to read book press 2:"))
if r1==2:
	this=''
	r=str(input("enter the file name:"))
	with open(r,'r') as f:
		data1=f.readlines()
		f.close()
	for i in data1:
		this=this+i
	print(this)
	this.strip()
	this.replace('\n'," ")
	speak(this)
cv2.imshow("roi", roi)
cv2.imshow("Img", img)
cv2.waitKey(0)
webcam.release()
cv2.destroyAllWindows()