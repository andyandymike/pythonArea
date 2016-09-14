import os
from markup import *

root = os.path.abspath('.')
file = open(root + '\\src.txt')
try:
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    parser.parse(file)
finally:
    file.close()