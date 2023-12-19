import os
import subprocess
import re


def create_dir(path):
	try:
		os.makedirs('apk')
	except OSError:
		print ("Создать директорию не удалось %s " %path)
	else:
		print ("Успешно создана директория %s " %path)
		return path , OSError


def ren_dir(path):
	commd = "rename 's/[ ()]/_/g' apk/*/"
	os.system (commd)
	commd = "rename 's/[ ()]/_/g' apk/*.apk"
	os.system (commd)
	return "Rename completed"

def exp_pack_txt(path):
	commd = f'find apk/*/ -type f | sort -f > "{path }/package-inst.txt"'
	os.system (commd)
	return "txt files creat"


path = os.getcwd()
path = os.path.dirname(__file__)
create_dir(path)
ren_dir(path)
exp_pack_txt(path)


pre_constr = []
pre_constr2 = []
path_arr = []
dir_name_arr = []
unic_dir_arr = []
rezult_path = []
f = open('package-inst.txt')
for line in f:
	path_arr.append(line.strip())
	pre_constr = line.split("/")
	dir_name_arr.append(pre_constr[1].strip())
f.close
for pice in range(len(dir_name_arr)-1):
	if dir_name_arr[pice]==dir_name_arr[pice+1]:
		pass
	else:
		unic_dir_arr.append(dir_name_arr[pice])
if dir_name_arr[len(dir_name_arr)-2]==dir_name_arr[len(dir_name_arr)-1]:
	pass
else:
	unic_dir_arr.append(dir_name_arr[len(dir_name_arr)-1])

print ("All line are processed")
for dir_name in unic_dir_arr:
	str_path = ""
	for path_apk in path_arr:
		if dir_name in path_apk:
			str_path += " "+path_apk
	rezult_path.append(str_path)

for line_rez in rezult_path:
    commd = f'adb install-multiple {line_rez}'
    os.system (commd)
    print (commd)
print ("All line are processed")
