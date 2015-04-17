#!/usr/bin/env python
import urllib3
import re
import os
import subprocess
import datetime
import pickle
http = urllib3.PoolManager()



# currentimageurl = None
# currenturlfile = 'currentimage.dat'
# currenturlopen = open(currenturlfile, 'rb')
# currentimageurl = pickle.load(currenturlopen)

natgeourl = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
imagepage = http.urlopen('GET', natgeourl, preload_content=False)

photodayfinder = re.compile('//images.nationalgeographic.com/wpf/media-live/photos/000/896/cache/\S*.jpg')
counter = 0
for y in imagepage:
    z = str(y)
    x = photodayfinder.findall(z)
    if x != []:
        nextimageurl = x[0]
        nextimageurl = 'http:' + nextimageurl
        print(nextimageurl)
        break
# http://images.nationalgeographic.com/wpf/media-live/photos/000/896/cache/spinner-dolphins-hawaii_89672_990x742.jpg
# if nextimageurl != currentimageurl:
#     try:
#         previouspage = urlopen(currentimageurl)
#         previouspic = previouspage.read()
#         now = datetime.datetime.now()
#         previousimagefname = 'imageoftheday{}-{}-{}.jpg'.format(now.month, (now.day-1), now.year)
#         fout1 = open(previousimagefname, "wb")
#         fout1.write(previouspic)
#         fout1.close()
#         
#     except:
#         x = "Do Nothing"
# 
#     currenturlfile = '/Users/kevin/Pictures/Imageoftheday/currentimage.txt'
#     currentimage = open(currenturlfile,'wb')
#     pickle.dump(nextimageurl, currentimage)
#     currentimage.close()


picturepage = http.urlopen('GET', nextimageurl, preload_content=False)
picture = picturepage.read()

imagefile = '/home/kevin/Projects/Image_of_the_Day/imageoftheday.jpg'
fout2 = open(imagefile, "wb")
fout2.write(picture)
fout2.close()


SCRIPT = "gsettings set org.gnome.desktop.background picture-uri file:///home/kevin/Projects/Image_of_the_Day/imageoftheday.jpg"
subprocess.Popen(SCRIPT, shell = True)

#        test = textsender(8173126800,'Wallpaper Updated')
print('Wallpaper Updated')

# else:
#     print('No new image')
#        test = textsender(8173126800,'No new image')
##except Exception as inst:
###    test = textsender(8173126800,inst)
##    print(inst)


