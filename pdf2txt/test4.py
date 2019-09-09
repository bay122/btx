from PIL import Image
import pytesseract
import cv2
import os

def parse(image_path, threshold=False, blur=False):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if threshold:
        gray = cv2.threshold(gray, 0, 255, \
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    if blur: #useful if salt-and-pepper background.
        gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray) #Create a temp file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename) #Remove the temp file
    text = text.split() #PROCESS HERE.
    print(text)
a = parse(image_path, True, False)
