import os
import subprocess

def create_dir1(path):
	try:
		os.makedirs('apk')
	except OSError:
		print ("Создать директорию не удалось %s " % path)
	else:
		print ("Успешно создана директория %s " % path)
		return path , OSError

def create_dir2(path):
	try:
		os.makedirs('test')
	except OSError:
		print ("Создать директорию не удалось %s " % path)
	else:
		print ("Успешно создана директория %s " % path)
		return path , OSError


path = os.getcwd()
path = os.path.dirname(__file__)
create_dir1(path)
create_dir2(path)

commd = "find apk/*/ -type d > test/test.txt"
os.system (commd)
f = open('test/test.txt')
name_arr = []
for line in f:
	name_arr.append(line.replace("apk/", "").strip())
f.close()
print (name_arr)
name_arr2 = []
for reline in name_arr:
	name_arr2.append(reline.replace("/", "").strip())
print (name_arr2)
for filine in name_arr2:
	rcomm = "rename -d 's/" + filine + "_/""/' apk/*/*.apk"
	print(rcomm)	
	os.system(rcomm)
	

print ("All line are processed")


