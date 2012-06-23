#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2
#test
from urllib.request import urlopen
import re
import os
import subprocess
import datetime
import pickle

def textsender(number,message):

    import smtplib

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'kevin.mclaughlin70@gmail.com', '1/2mv^2+1/2kx^2=E' )

    server.sendmail( 'kevin', '{0}@mms.att.net'.format(number), '{0}'.format(message) )


currentimageurl = "None"
currenturlfile = '/Users/kevin/Pictures/Imageoftheday/currentimage.txt'
currenturlopen = open(currenturlfile, 'rb')
currentimageurl = pickle.load(currenturlopen)

natgeourl = 'http://photography.nationalgeographic.com/photography/photo-of-the-day/'
imagepage = urlopen(natgeourl)

photodayfinder = re.compile('http://images.nationalgeographic.com\S*.jpg')
for y in imagepage:
    z = str(y)
    x = photodayfinder.findall(z)
    if x != []:
        nextimageurl = x[0]
        break

if nextimageurl != currentimageurl:
    try:
        previouspage = urlopen(currentimageurl)
        previouspic = previouspage.read()
        now = datetime.datetime.now()
        previousimagefname = '/Users/kevin/Pictures/Imageoftheday/imageoftheday{}-{}-{}.jpg'.format(now.month, (now.day-1), now.year)
        fout1 = open(previousimagefname, "wb")
        fout1.write(previouspic)
        fout1.close()
        
    except:
        x = "Do Nothing"

    currenturlfile = '/Users/kevin/Pictures/Imageoftheday/currentimage.txt'
    currentimage = open(currenturlfile,'wb')
    pickle.dump(nextimageurl, currentimage)
    currentimage.close()


    picturepage = urlopen(nextimageurl)
    picture = picturepage.read()

    imagefile = '/Users/kevin/Pictures/Imageoftheday/imageoftheday.jpg'
    fout2 = open(imagefile, "wb")
    fout2.write(picture)
    fout2.close()


    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to {MacintoshHD/Users/kevin/Pictures/Imageoftheday/imageoftheday.jpg"} as alias
    end tell
    END"""
    subprocess.Popen(SCRIPT, shell = True)

    killallcommand = 'killall Dock'
    subprocess.Popen(killallcommand, shell = True)
#        test = textsender(8173126800,'Wallpaper Updated')
    print('Wallpaper Updated')

else:
    print('No new image')
#        test = textsender(8173126800,'No new image')
##except Exception as inst:
###    test = textsender(8173126800,inst)
##    print(inst)


