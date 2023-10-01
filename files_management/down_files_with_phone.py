import os
import time
import colorama
from colorama import Fore, Style, Back

def PC_path():
	try:
		print (Fore.GREEN)
		print ("You can input PC path manual")
		print(Style.RESET_ALL)
		PC_path = input ("PC path of phone: ")
		print("OK")
		if PC_path =="":
			PC_path	= "."
		print(PC_path)
	except OSError:
		print ("Don`t read path ")
	else:
		print ("Function back PC path ", BP_path[0])
		return PC_path , OSError

def base_phone_path(path):
	try:
		BPpath_file = path +"/base_path_phone.txt"
		f=open(BPpath_file, "r")
		BP_path = f.read().strip()
	except OSError:
		print ("Don`t read path ")
	else:
		print ("Function back base phone path ", BP_path)
		return BP_path , OSError

def final_phone_path():
	try:
		print (Fore.RED)
		print ("1 - bluetooth")
		print ("2 - DCIM")
		print ("3 - documents")
		print ("4 - Download")
		print ("5 - Fonts")
		print ("6 - inshot")
		print ("7 - MIUI/sound_recorder")
		print ("8 - Movies")
		print ("9 - Music")
		print ("10 - Pictures")
		print ("11 - Ringtones")
		print ("12 - Telegram")
		print ("13 - viber")
		print ("14 - Whatsapp/media")
		print ("15 - youcut")
		print ("100 - /data/data/com.termux/files/home")
		print ("all - Copy all items")
		print(Style.RESET_ALL)
		choise = input ("Choise of the Directory for copy : ")

		if choise == "1":
			FP_path = "bluetooth"
		elif choise == "2":
			FP_path = "DCIM"
		elif choise == "3":
			FP_path = "documents"
		elif choise == "4":
			FP_path = "Download"
		elif choise == "5":
			FP_path = "Fonts"
		elif choise == "6":
			FP_path = "inshot"
		elif choise == "7":
			FP_path = "MIUI/sound_recorder"
		elif choise == "8":
			FP_path = "Movies"
		elif choise == "9":
			FP_path = "Music"
		elif choise == "10":
			FP_path = "Pictures"
		elif choise == "11":
			FP_path = "Ringtones"
		elif choise == "12":
			FP_path = "Telegram"
		elif choise == "13":
			FP_path = "viber"
		elif choise == "14":
			FP_path = "Whatsapp/Media"
		elif choise == "15":
			FP_path = "youcut"
		elif choise == "100":
			FP_path = "/data/data/com.termux/files/home"
		elif choise == "all":
			FP_path = "/data/data/com.termux/files/home"
	except OSError:
		print ("Don`t read path ")
	else:
		print (Fore.BLUE)
		print ("Function back final phone path: ", FP_path)
		print(Style.RESET_ALL)
		return FP_path , choise, OSError

#adb pull /storage/emulated/0/DCIM/Screenshots/ /media/korolevsa/Files/55/1\ NTFS/sort/перенос\ файлов/DCIM/

try:
	path = os.getcwd()
	BP_path = "/storage/emulated/0"
	BP_path = base_phone_path(path)
	print (Fore.BLUE)
	print ("default base path of phone = " + BP_path[0])
	print ("You can input base path manual")
	print(Style.RESET_ALL)
	rez_inp = input ("Base path of phone: ")
	print(BP_path[0])
	print("OK")
	if rez_inp !="":
		BP_path	= rez_inp
	FP_path = final_phone_path()
	PC_path = PC_path()
	print(FP_path[1])

	if FP_path[1] == "bluetooth" or FP_path[1] == "DCIM" or FP_path[1] == "documents" or FP_path[1] == "Download" or FP_path[1] == "Fonts" or FP_path[1] == "inshot" or FP_path[1] == "MIUI/sound_recorder" or FP_path[1] == "Movies" or FP_path[1] == "Music" or FP_path[1] == "Pictures" or FP_path[1] == "Ringtones" or FP_path[1] == "Telegram" or FP_path[1] == "viber" or FP_path[1] == "Whatsapp/Media" or FP_path[1] == "youcut" or FP_path[1] == "/data/data/com.termux/files/home":
		print (Fore.MAGENTA)
		print("su adb pull "+ FP_path[0] +" "+ PC_path[0])
		os.system("su adb pull " + FP_path[0] +" "+ PC_path[0])
		print(Style.RESET_ALL)
	else:
		print (Back.MAGENTA + Fore.YELLOW + Style.BRIGHT)
		print("adb pull "+ BP_path[0] + "/" + FP_path[0] +" "+ PC_path[0])
		os.system("adb pull "+ BP_path[0] + "/" + FP_path[0] +" "+ PC_path[0])
		print(Style.RESET_ALL)

except OSError:
	print ("Runtime error")
else:
	print ("Success")



print ("All line are processed")
