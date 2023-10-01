import os
import time

# function create main work dir for App
def create_dir(path):
	try:
		os.makedirs('apk/')
		os.makedirs('tmp_for_script/down_apk/')
	except OSError:
		print ("Создать директорию %s не удалось, возможно уже создана" % path)
	else:
		print ("Успешно создана директория %s/apk" % path)
		return path , OSError

# function for generate file with list user App
def list_apk():
	commd = "adb shell pm list packages -3 > tmp_for_script/list_usr_apk.txt"
	os.system (commd)
	return "txt files creat"

# function generate array with list pull app library from android
def list_app(path):
	print ("1")
	commd = "ls tmp_for_script/down_apk/ > " + path +"/tmp_for_script/package-tmp-ren.txt"
	os.system (commd)
	fs = open('tmp_for_script/package-tmp-ren.txt')
	ren_arr=[]
	for app_name in fs:
		ren_arr.append(app_name.strip())
	fs.close()
	return ren_arr

def ren_app(ren_arr, data, path_for_app):
	for name_app in ren_arr:
		source_name = 'tmp_for_script/down_apk/'+ name_app
		destanation_name = 'tmp_for_script/down_apk/'+ data + '_'+ name_app
		print(source_name, destanation_name	)
		os.rename(source_name, destanation_name)
	summary_path = 	"mv tmp_for_script/down_apk/*.apk " + path_for_app
	os.system(summary_path)
	return "Great works!"

# main function of script
def pull_apk():
# Generate user_arr with list app of user
	f = open('tmp_for_script/list_usr_apk.txt')
	user_arr=[]
	for line in f:
		user_arr.append(line.replace("package:", "").strip())
	f.close()	
# start cycle 
	for data in user_arr:
# create directory with nape one user App
		path_for_app = "apk/" + data
		try:
			os.makedirs(path_for_app)
		except OSError:
			print ("Создать директорию %s не удалось, возможно уже создана" % path_for_app)
		else:
			print ("Успешно создана директория %s/apk" % path_for_app)
#Create file with list of name path pull App				
		commd = "adb shell pm path " + data + " > tmp_for_script/path_apk.txt"
		os.system (commd)
#Create path_arr with list of path App to pull
		t = open('tmp_for_script/path_apk.txt')
		path_arr=[]
		for path_line in t:
			path_arr.append(path_line.replace("package:", "").strip())
		t.close()
#Downloads App librarry	in tmp	
		for path_down in path_arr:
			commd_down = "adb pull " + path_down + " " + path + "/tmp_for_script/down_apk/"
			os.system (commd_down)
#Create ren_arr with list app library for rename
		print("2")
		ren_arr = list_app(path)
#Rename file
		ren_app(ren_arr, data, path_for_app)
	return path , OSError


try:
	path = os.getcwd()
	create_dir(path)
	list_apk()
	pull_apk()
	
	
except OSError:
	print ("Runtime error")
else:
	print ("Success")
	

print ("All line are processed")
