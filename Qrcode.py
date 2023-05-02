
# How to RUN the CLI:
# syntax:
# python QRcode.py <Text/Link to be converted> <Name to be saved as> <Path to be saved to>

import PIL
import qrcode
import argparse
from pathlib import Path

# Creating Parser for CLI
parser = argparse.ArgumentParser()

# Adding all the functions
parser.add_argument("link")
parser.add_argument("name")
parser.add_argument("path",nargs='?',const="C:/Users/amanv/Desktop/",default="C:/Users/amanv/Desktop/")

# Retrive Data from the CLI
args = parser.parse_args()

data=args.link

# Creating and Saving the QRCOde
img=qrcode.make(data)
img.save(args.path+"/"+args.name+".png")

# Opening the QRCode
PIL.Image.open(args.path+args.name+".png",mode='r').show()
