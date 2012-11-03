import subprocess

SCRIPT = """/usr/bin/osascript<<END
path to user domain
END"""


x = subprocess.check_output(SCRIPT, shell = True)
print(x)
##
##killallcommand = 'killall Dock'
##subprocess.Popen(killallcommand, shell = True)
