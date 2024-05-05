import pytesseract
from pytesseract import Output
import PIL.Image
import cv2


myconfig=r"--psm 11 --oem 3"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# text=pytesseract.image_to_string(PIL.Image.open("sample.jpg"), config=myconfig)
# print(text)

img=cv2.imread("test.jpg")
height,width,_=img.shape

boxes=pytesseract.image_to_boxes(img,config=myconfig)
# print(boxes)

# for box in boxes.splitlines():
#     box=box.split(" ")
#     img=cv2.rectangle(img,(int(box[1]),height-int(box[2])),(int(box[3]),height-int(box[4])),(0,255,0),2)

data=pytesseract.image_to_data(img,config=myconfig,output_type=Output.DICT)

lbox=len(data['text'])
for i in range(lbox):
    if float(data['conf'][i])>80:
        (x,y,w,h)=(data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        img=cv2.putText(img,data['text'][i],(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2,cv2.LINE_AA)

cv2.imshow("img",img)
cv2.waitKey(0)
