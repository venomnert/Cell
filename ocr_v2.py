from PIL import Image
import pytesseract
import pyautogui as gui
import datetime
import os
import argparse
import sys

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

def init(todayDirectory, args):
    counter = True
    digitTop = 162
    digitLeft = 665
    digitWidth = 100
    digitHeight = 14
    boughtPriceThreshold = 0.3
    stockName, boughtPrice, thresholdType, thresholdValue = initValues(args)
    sellHalf.has_been_called = False
    boughtStock = False

    while(counter):
        img = gui.screenshot(
            region=(digitLeft, digitTop, digitWidth, digitHeight))
        try:
            guess = pytesseract.image_to_string(
                img, config="-psm 6").replace(" ", "")
            price = float(guess)
            saveImg(img, todayDirectory, guess, 'true', 'png')
        except ValueError:
            wrongGuess = pytesseract.image_to_string(img, config="-psm 6")
            print(wrongGuess)
            saveImg(img, todayDirectory, wrongGuess, 'false', 'png')
            continue

        if not boughtStock:
            if (boughtPrice <= price <= boughtPrice + boughtPriceThreshold):
                boughtPrice = price
                buyAll()
                boughtStock = True
        else:
            if (price - boughtPrice >= (thresholdValue * 2)):  # scenario 4
                sellAll(price)
            elif (price - boughtPrice >= thresholdValue):  # scenarion 1 & 2
                if (sellHalf.has_been_called):
                    if (price <= boughtPrice + thresholdValue):
                        sellAll(price)
                else:
                    sellHalf()
            elif (price - boughtPrice < (-1 * thresholdValue)):  # scenario 3
                sellAll(price)
            

def initValues(args):
    stockName = args['stock']
    boughtPrice = float(args['bought_price'])
    
    if args['thresholdtype'] or args['thresholdvalue'] is not None:
        thresholdType = args['thresholdtype']
        thresholdValue = float(args['thresholdvalue'])/ 100 if thresholdType == 'percentage' else float(args['thresholdvalue'])
    else:
        thresholdType = 'amount'
        thresholdValue = 0.1

    return [stockName, boughtPrice, thresholdType, thresholdValue]

def imgFolder():
    currDate = datetime.date.today().strftime("%Y-%m-%d")
    if not os.path.exists(currDate):
        os.makedirs(currDate)
    return currDate

def saveImg(img, rootDirectory, guess, guessType, imgType):
    guess = guess.replace('\\', '-').replace('//', '-').replace(':', '-').replace('*', "-").replace(
        '?', "-").replace("\"", "-").replace("<", "-").replace(">", "-").replace("|", "-")

    fileName = datetime.datetime.now().strftime("%H-%M-%S") + \
        '-' + guess + '-' + guessType + '.' + imgType
    try:
        img.save(os.path.abspath(os.path.join(rootDirectory, fileName)))
    except OSError:
        fileName = datetime.datetime.now().strftime("%H-%M-%S") + \
            '-' + guessType + '.' + imgType
        img.save(os.path.abspath(os.path.join(rootDirectory, fileName)))

def sellHalf():
    sellHalf.has_been_called = True
    gui.click(x=881, y=514, clicks=1, button='left')

def sellAll(price):
    gui.click(x=677, y=510, clicks=1, button='left')
    print('final price', price)
    sys.exit("Sold All Stock!")

def buyAll():
    gui.click(x=885, y=479, clicks=1, button='left')
    print('Bought stock')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--stock", required=True,
                    help="Enter the purchased stock name or ticker")
    ap.add_argument("-p", "--bought_price", required=True,
                    help="Enter the price the stock was bought")
    ap.add_argument("-tt", "--thresholdtype", required=False,
                    help="Enter the price the stock was bought")
    ap.add_argument("-tv", "--thresholdvalue", required=False,
                    help="Enter the value of the threshold '1%' or '1 cents' ")
    args = vars(ap.parse_args())
    print(args)

    todayDirectory = imgFolder()
    init(todayDirectory, args)

if __name__ == '__main__':
    main()


# sell location: (677, 510)
# sell-half location: (881, 514)
# buy location: (885, 479)
