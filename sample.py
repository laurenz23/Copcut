import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread(r'C:\Users\franc\Pictures\mek3.PNG') 

cv2.imshow('normal', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
print(pytesseract.image_to_string(gray))
cv2.waitKey(0)
cv2.destroyAllWindows()