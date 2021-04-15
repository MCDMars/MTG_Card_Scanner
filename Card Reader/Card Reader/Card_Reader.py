"""

import cv2
import pytesseract

# Refer to pytesseract install
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

# Read image

img = cv2.imread ("bolt.jpg")

# Preprocessing

# Convert to grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size
# The kernel size will change the area being detected
# Smaller values may pick up individual words as opposed to sentences

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Apply dilation on the threshold image

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Find contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create image copy

img2 = img.copy()

# Create text file to hopefully display recognized words
file = open("words.txt", "w+")
file.write("")
file.close()

# Loop through the contours, crop rectangle, then pass into pytesseract to extract text, and write to file

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Crop the text block for giving input to text reader
    cropped = img2[y:y + h, x:x + w]

    # Open the text file in append mode to, again, hopefully display recognized words
    file = open("words.txt", "a")

    # Apply text reader on cropped iage
    text = pytesseract.image_to_string(cropped)

    # Append text to file
    file.write(text)
    file.write("\n")

    # Closed file
    file.close()



# Stuff to show image so I know what's happening at any given moment


cv2.imshow("card", dilation)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""

import PyPDF2

pdfFileObj = open("bolas.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)


print(pageObj.extractText())

pdfFileObj.close()