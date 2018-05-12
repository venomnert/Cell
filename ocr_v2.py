from PIL import Image
import pytesseract
import pyautogui as gui

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

counter = True
boughtPrice = 102.38

screenWidth, screenHeight = gui.size()
qtyPos = {'x': screenWidth * .2885, 'y': screenHeight * .1805}
orderTypePos = {'x': screenWidth * .3380, 'y': screenHeight * .1796}
# After first option the height difference for each option is 12
orderTypeOptionsPos = {
    'market': {'y': orderTypePos['y'] + 25},
    'limit': {'y': orderTypePos['y'] + 37},
    'stop': {'y': orderTypePos['y'] + 49},
    'stop_lmt': {'y': orderTypePos['y'] + 61}
}
limitPos = {'x': screenWidth * .4052, 'y': screenHeight * .1777}
buyPos = {'x': screenWidth * .6406, 'y': screenHeight * .1796}


def hotkey():
    gui.click(qtyPos['x'], qtyPos['y'], 3, interval=0.25, button='left')
    gui.typewrite('1000')

    gui.click(orderTypePos['x'], orderTypePos['y'], 1, button='left')
    gui.click(orderTypePos['x'], orderTypeOptionsPos['limit']
              ['y'], button='left', clicks=3, interval=0.25)

    gui.click(limitPos['x'], limitPos['y'], 3, interval=0.25, button='left')
    gui.typewrite('200')

    gui.click(buyPos['x'], buyPos['y'], 1, button='left')


while(counter):
    price = float(pytesseract.image_to_string(gui.screenshot(
        region=(135, 595, 80, 25)), config="-psm 6"))
    if (price - boughtPrice >= .10):
        counter = False
        # hotkey()
    print("Curr price: ", price)

print("Sold Price ", price)
