from PIL import Image
import pytesseract
import pyautogui as gui

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

counter = True
boughtPrice = 102.38

while(counter):
    price = float(pytesseract.image_to_string(gui.screenshot(
        region=(135, 595, 80, 25)), config="-psm 6"))
    if (price - boughtPrice >= .10):
        counter = False
    print("Curr price: ", price)

print("Sold Price ", price)
