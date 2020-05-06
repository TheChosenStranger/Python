import sys,os
from datetime import date

def FileHeader():
	today = date.today()
	d = today.strftime("%d-%m-%Y")
	name = input("Enter your name  ")
	header = "/******************************/\n/* Author  : "+name+" */\n/* Version : V1.0             */\n/* Date    : "+d+"         */\n/******************************/\n"
	return header

def DriverFiles(driver_name):
	header = FileHeader()
	interface = open(driver_name+"_interface.h",'w')
	interface.write(header)
	interface.write("#ifndef "+driver_name+'_INTERFACE_H_\n')
	interface.write("#define "+driver_name+'_INTERFACE_H_\n\n')
	interface.write("#endif"+"\n")
	interface.close()
	private = open(driver_name+"_private.h",'w')
	private.write(header)
	private.write("#ifndef "+driver_name+'_PRIVATE_H_\n')
	private.write("#define "+driver_name+'_PRIVATE_H_\n\n')
	private.write("#endif"+"\n")
	private.close()
	config = open(driver_name+"_config.h",'w')
	config.write(header)
	config.write("#ifndef "+driver_name+'_CONFIG_H_\n')
	config.write("#define "+driver_name+'_CONFIG_H_\n\n')
	config.write("#endif"+"\n")
	config.close()
	register = open(driver_name+"_register.h",'w')
	register.write(header)
	register.write("#ifndef "+driver_name+'_REGISTER_H_\n')
	register.write("#define "+driver_name+'_REGISTER_H_\n\n')
	register.write("#endif"+"\n")
	register.close()
	program = open(driver_name+"_program.c",'w')
	program.write(header)
	program.write('#include "STD_TYPES.h"\n')
	program.write('#include "BIT_MATH.h"\n\n')
	program.write("#include "+'"'+driver_name+'_interface.h"\n')
	program.write("#include "+'"'+driver_name+'_register.h"\n')
	program.write("#include "+'"'+driver_name+'_config.h"\n')
	program.write("#include "+'"'+driver_name+'_private.h"\n')
	program.close()
	return


def DriverFolder():
	old_folders=os.listdir()
	user_driver = input("What is the name of your driver  ")
	if old_folders==[]:
		os.mkdir("01"+"_"+user_driver)
		os.chdir("01"+"_"+user_driver)
	else:
		last_folder_name = old_folders[len(old_folders)-1].split('_')[0]
		if int(last_folder_name) < 9:
			os.mkdir("0"+str(int(last_folder_name)+1)+"_"+user_driver)
			os.chdir("0"+str(int(last_folder_name)+1)+"_"+user_driver)
		else:
			os.mkdir(str(int(last_folder_name)+1)+"_"+user_driver)
			os.chdir(str(int(last_folder_name)+1)+"_"+user_driver)
	DriverFiles(user_driver)
	return

def DriverCreator():
	print("Welcome to the Driver Files Creator V2")
	user_layer = input("In which layer does your driver exist  ")
	if user_layer.lower() == "mcal":
		os.chdir("01_MCAL")
	elif user_layer.lower() == "hal":
		os.chdir("02_HAL")
	elif user_layer.lower() == "app":
		os.chdir("03_APP")
	elif user_layer.lower() == "lib":
		os.chdir("04_LIB")
	elif user_layer.lower() == "srv":
		os.chdir("05_SRV")
	elif user_layer.lower() == "mem":
		os.chdir("06_MEM")
	elif user_layer.lower() == "os":
		os.chdir("07_OS")
	else:
		print("<"+user_layer +">"+" Wrong input: layer doesn't exist")
		return
	DriverFolder()
	return 

if __name__ == '__main__':
  DriverCreator() 