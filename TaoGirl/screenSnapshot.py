from PIL import ImageGrab
import os

bbox = (100,100,500,500)
pic = ImageGrab.grab(bbox)
if os.path.isfile('snapshot.jpg'):
    os.remove('snapshot.jpg')
pic.save('snapshot.jpg')