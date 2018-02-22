from pytesseract import *
from PIL import Image

image = Image.open("captcha.png")

text = image_to_string(image)

print(text)
