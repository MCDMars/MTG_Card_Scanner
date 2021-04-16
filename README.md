# MTG_Card_Scanner
The goal of this project is to be able to take an image of any magic the gathering card, and output data such as the name, card type, and the set it's from

Right now, the main idea is to be able to only read from certain areas of the image, as the program in its current state tries to read the whole thing at once, which is messing it up. 

I also want to try making it so that the image to represent the set is easily read, and compare to a teach set of all set symbols, hopefully even figure out how to read the colour properly to determine rarity

A future idea is to be able to make it recognise a magic card from an image, so that they could be scanned and read on realtime video, but for the most part, from a still image of a few, or even just one, from a table would be good enough

# Requirements

OpenCV Python https://pypi.org/project/opencv-python/
Tesseract https://github.com/tesseract-ocr/tesseract
Pytesseract https://pypi.org/project/pytesseract/
