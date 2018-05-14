from PIL import Image
import pytesseract
import pyautogui as gui

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#Left, Top, Width, Height
# doc: http://pyautogui.readthedocs.io/en/latest/screenshot.html
# how to save: https://www.programcreek.com/python/example/103348/pyautogui.screenshot
# gui.screenshot(region=(135, 595, 80, 25)).save('test_6' + '.png')
im = Image.open("./img/ls_4.jpeg")
text = pytesseract.image_to_string(im, config="-psm 6")
print(text)

# Install pytesseract for windows: https://github.com/UB-Mannheim/tesseract/wiki
# Resolve the issue that you will run into: https://stackoverflow.com/questions/34225927/pytesseract-cannot-find-the-file-specified
# How to read numbers using pytesseract https://stackoverflow.com/questions/42881884/python-read-number-in-image-with-pytesseract
# In order improve accuracy improve the image size by increasing the font size and changing the font family to the following: arial, bold, 16. Black background and font is in white
# Inspiration for the above idea came to my by reading the first post: https://news.ycombinator.com/item?id=14741124


# V2:
# Improve accuracy of OCR
# When it goes beyond the thershold sell 1/2 of share to make profit
# If it doubles the threshold sell all of the share
