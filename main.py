from PIL import Image, ImageDraw, ImageFont

target = input("滑稽今天说了啥：")
text = list(target)

def isAscii(char):
    try:
        char.encode('ASCII')
        return True
    except UnicodeError:
        return False


lang = []
for char in text:
    if isAscii(char):
        lang.append(True)
    else:
        lang.append(False)

asciiLen = sum(true for true in lang)
otherLen = len(lang) - asciiLen
textLen = (otherLen * 2) + asciiLen

# Image width: 20 ascii char
space = 20 - textLen
if space < 0:
    raise "Target text too long"
elif space == 0:
    startPoint = 0
else:
    startPoint = space / 2

img = Image.open("./huaji.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./STHeitiMedium.ttc", 18)

draw.text((startPoint * 9.6, 90), target, font=font, align="center", fill="#000000")
img.show()
img.save(f"./滑稽说{target}.jpg")