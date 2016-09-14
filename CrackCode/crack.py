from PIL import Image
import os


root = os.path.abspath('.')
imageFileLoc = root + '\\wm.gif'
im = Image.open(imageFileLoc)
im = im.convert('P')
im2 = Image.new('P', im.size, 255)

his = im.histogram()

values = {}
for i in range(256):
    values[i] = his[i]

sortedValues = sorted(values.items(), key=lambda x:x[1], reverse=True)
#print(sortedValues[:10])

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pix = im.getpixel((x,y))
        if pix == 6: # these are the numbers to get
            im2.putpixel((x,y),0)

#im2.show()

inletter = False
foundletter = False

start = 0
end = 0
letters = []

for x in range(im2.size[0]):
    for y in range(im2.size[1]):
        if im2.getpixel((x,y)) != 255:
            inletter = True
            break

    if foundletter == False and inletter == True:
        foundletter = True
        start = x

    if foundletter == True and inletter == False:
        foundletter = False
        end = x
        letters.append((start,end))

    inletter=False

count = 0
for letter in letters:

    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
    im3.save('./%s.gif' % (count))
    count += 1

def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

_0gif = Image.open('0.gif')
print(buildvector(_0gif))