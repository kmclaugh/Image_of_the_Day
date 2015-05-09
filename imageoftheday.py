#!/usr/bin/env python
import urllib3
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
import os
import subprocess
import datetime
import pickle
http = urllib3.PoolManager()
import easygui


natgeourl = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
imagepage = http.urlopen('GET', natgeourl, preload_content=False)
parsed_html = BeautifulSoup(imagepage)
primary_photo_div = parsed_html.body.find('div', attrs={'class':'primary_photo'})
image_tag = primary_photo_div.find('img')
image_src = image_tag['src']
image_src = image_src[2:]
current_image_file = open('/home/kevin/Projects/Image_of_the_Day/currentimage.dat', 'rb')
current_image = pickle.load(current_image_file)

if image_src != current_image:

    picturepage = http.urlopen('GET', image_src, preload_content=False)
    picture = picturepage.read()
    
    imagefile = '/home/kevin/Projects/Image_of_the_Day/imageoftheday.jpg'
    fout2 = open(imagefile, "wb")
    fout2.write(picture)
    fout2.close()
    
    
    SCRIPT = "gsettings set org.gnome.desktop.background picture-uri file:///home/kevin/Projects/Image_of_the_Day/imageoftheday.jpg"
    subprocess.Popen(SCRIPT, shell = True)
    
    print('Wallpaper Updated', image_tag['alt'])
    current_image_file = open('/home/kevin/Projects/Image_of_the_Day/currentimage.dat', 'wb')
    pickle.dump(image_src, current_image_file)
    
    easygui.msgbox(image_tag['alt'], title="Image of the Day")


