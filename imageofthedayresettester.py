#!/usr/bin/env python
import urllib3
import os
import subprocess
import pickle
http = urllib3.PoolManager()

testpicurl = 'http://images.nationalgeographic.com/wpf/media-live/photos/000/896/cache/camino-pilgrimage-george_89658_990x742.jpg'


picturepage = http.urlopen('GET', testpicurl, preload_content=False)
picture = picturepage.read()

imagefile = '/home/kevin/Projects/Image_of_the_Day/imageoftheday.jpg'
fout2 = open(imagefile, "wb")
fout2.write(picture)
fout2.close()


currenturlfile = 'currentimage.dat'
currentimage = open(currenturlfile,'wb')
pickle.dump(testpicurl, currentimage)
currentimage.close()

SCRIPT = "gsettings set org.gnome.desktop.background picture-uri file://imagefile.jpg"
subprocess.Popen(SCRIPT, shell = True)

