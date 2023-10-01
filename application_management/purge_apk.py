import os
f = open('package-list-del.txt')
for line in f:
    commd = "adb shell pm uninstall --user 0 "+ line
    os.system (commd)
    print ("Delete ", line)
print ("All line are processed")
