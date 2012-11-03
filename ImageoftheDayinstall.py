import os

currentdir = os.getcwd()

dirname = "ImageoftheDay"

try:
    os.mkdir("./" + dirname + "/")
except:
    print('The ImageoftheDay Folder already exists. Please delete it and retry installation")

SCRIPT = """usr/bin/osascript<<END
