from urllib.request import urlopen
import os
import subprocess
import pickle


testpicurl = 'http://ngm.nationalgeographic.com/ngm/100best/images/multi1_main.jpg'


picturepage = urlopen(testpicurl)
picture = picturepage.read()

imagefile = '/Users/kevin/Pictures/Imageoftheday/imageoftheday.jpg'
fout2 = open(imagefile, "wb")
fout2.write(picture)
fout2.close()


currenturlfile = '/Users/kevin/Pictures/Imageoftheday/currentimage.txt'
currentimage = open(currenturlfile,'wb')
pickle.dump(testpicurl, currentimage)
currentimage.close()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to {MacintoshHD/Users/kevin/Pictures/Imageoftheday/imageoftheday.jpg"} as alias
end tell
END"""
subprocess.Popen(SCRIPT, shell = True)

killallcommand = 'killall Dock'
subprocess.Popen(killallcommand, shell = True)
