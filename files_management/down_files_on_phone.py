import os
import time
import colorama
from colorama import Fore, Style

def PC_path():
	try:
		print (Fore.GREEN)
		print ("You can input PC path manual")
		print(Style.RESET_ALL)
		BPC_path = input ("PC path of phone: ")
		print("OK")
		if BPC_path =="":
			BPC_path	= "."
		print(BPC_path)
	except OSError:
		print ("Don`t read path ")
	else:
		print ("Function back PC path ", BPC_path[0])
		return BPC_path , OSError

def base_phone_path(path):
	try:
		BPpath_file = path +"/base_path_phone.txt"
		f=open(BPpath_file, "r")
		P_path = f.read().strip()
	except OSError:
		print ("Don`t read path ")
	else:
		print ("Function back phone path ", P_path)
		return P_path , OSError

def final_pc_path():
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
		print ("100 - /media/korolevsa/Files/55/1\ NTFS/sort/перенос\ файлов")
		print ("all - DCIM/CapCut")
		print(Style.RESET_ALL)
		choise = input ("Choise of the Directory for copy : ")

		if choise == "1":
			FPC_path = "bluetooth"
		elif choise == "2":
			FPC_path = "DCIM"
		elif choise == "3":
			FPC_path = "documents"
		elif choise == "4":
			FPC_path = "Download"
		elif choise == "5":
			FPC_path = "Fonts"
		elif choise == "6":
			FPC_path = "inshot"
		elif choise == "7":
			FPC_path = "MIUI/sound_recorder"
		elif choise == "8":
			FPC_path = "Movies"
		elif choise == "9":
			FPC_path = "Music"
		elif choise == "10":
			FPC_path = "Pictures"
		elif choise == "11":
			FPC_path = "Ringtones"
		elif choise == "12":
			FPC_path = "Telegram"
		elif choise == "13":
			FPC_path = "viber"
		elif choise == "14":
			FPC_path = "Whatsapp/Media"
		elif choise == "15":
			FPC_path = "youcut"
		elif choise == "100":
			FPC_path = "/media/korolevsa/Files/55/1\ NTFS/sort/перенос\ файлов"
		elif choise == "all":
			FPC_path = "/DCIM/CapCut"
	except OSError:
		print ("Don`t read path ")
	else:
		print (Fore.BLUE)
		print ("Function back final PC path: ", FPC_path)
		print(Style.RESET_ALL)
		return FPC_path , choise, OSError

try:
	path = os.getcwd()
	P_path = "/storage/emulated/0"
	P_path = base_phone_path(path)
	print (Fore.BLUE)
	print ("default path of phone = " + P_path[0])
	print ("You can input phone path manual")
	print(Style.RESET_ALL)
	rez_inp = input ("Path of phone: ")
	print(P_path[0])
	print("OK")
	if rez_inp !="":
		P_path	= rez_inp
	FPC_path = final_pc_path()
	PC_path = PC_path()
	print(FPC_path[1])

	if FPC_path[1] == "100" or FPC_path[1] == "101" or FPC_path[1] == "102" or FPC_path[1] == "103" or FPC_path[1] == "104" or FPC_path[1] == "105":
		print (Fore.YELLOW)
		print("su adb push "+ PC_path[0] + " " + P_path[0])
		os.system("su adb push " + PC_path[0] + " " + P_path[0])
		print(Style.RESET_ALL)
	else:
		print (Fore.YELLOW)
		print("adb push " + PC_path[0] + "/" + FPC_path[0] + " " + P_path[0])
		os.system("adb push " + PC_path[0]  + "/" + FPC_path[0] + " " + P_path[0])
		print(Style.RESET_ALL)

except OSError:
	print ("Runtime error")
else:
	print ("Success")



print ("All line are processed")
