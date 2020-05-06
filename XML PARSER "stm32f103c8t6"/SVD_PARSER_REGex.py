import sys,os,re
from os import path

def ParseField(line,peripheral_file,register_size):
	if re.search(r'<bitOffset>([\d]*)</bitOffset>',line) and re.search(r'<bitWidth>([\d]*)</bitWidth>',line):
		field_name = re.search(r'<name>([\w]*)</name>',line)
		field_name = field_name.group(1)
		field_offset = re.search(r'<bitOffset>([\d]*)</bitOffset>',line)
		field_offset = field_offset.group(1)
		field_width = re.findall(r'<bitWidth>([\d]*)</bitWidth>',line)
		field_width = field_width[0]
		mask =  0
		for x in range(0,int(field_width)):
			mask =  mask +2**x
		mask = mask *2**(int(field_offset))
		mask = "0x%0.8X" % mask
		if re.findall(r'<access>([\w-]*)</access>',line):
			field_access = re.findall(r'<access>([\w-]*)</access>',line)
			field_access = field_access[0]
		else:
			field_access = "write"
		if int(field_width) == 1:
			if field_access.find("write") != -1:
				peripheral_file.write("#define\t"+field_name+"_MASK\t\t\t\t\t("+mask+")\n")
			else:
				peripheral_file.write("#define\t"+field_name+"_READ_MASK\t\t\t("+mask+")\n")
		else:
			if field_access.find("write") != -1:
				peripheral_file.write("#define\t"+field_name+"_CLEAR_MASK\t\t\t("+mask+")\n")
			else:
				peripheral_file.write("#define\t"+field_name+"_READ_MASK\t\t\t("+mask+")\n")
	return

def ParseRegister(register,peripheral_file,struct_temp):
	register_name = re.search(r'<name>([\w]*)</name>',register)
	register_name = register_name.group(1)
	register_base = re.search(r'<addressOffset>([A-Za-z0-9]+)</addressOffset>',register)
	register_base = register_base.group(1)
	register_size = re.search(r'<size>([A-Za-z0-9]+)</size>',register)
	register_size = register_size.group(1)
	register_size = str(int(register_size,16))
	if re.search(r'<description>([\w]*)</description>',register):
		register_comm = re.search(r'<description>([\w]*)</description>',register)
		register_comm = register_comm.group(1)
	else:
		register_comm = "/**/"
	struct_temp = struct_temp +"\tu"+register_size+"\t"+register_name+";\t/*"+register_comm+"*/\n"
	fields = ""
	found = 0
	for line in register.split("<field>"):
		ParseField(line,peripheral_file,register_size)
	return struct_temp

def ParsePeripheral(peripheral):
	peripheral_name = re.search(r'<name>([\w]*)</name>',peripheral)
	peripheral_name = peripheral_name.group(1)
	peripheral_file = open(peripheral_name+"_register.h",'w')
	peripheral_file.write("/*This file was made by Moustafa Ghareeb*/\n")
	peripheral_base = re.search(r'<baseAddress>([A-Za-z0-9]+)</baseAddress>',peripheral)
	peripheral_base = peripheral_base.group(1)
	struct_temp = "\ntypedef struct "+peripheral_name+"_\n{\n"
	registers = ""
	found = 0
	peripheral_file.write("/*Defining all main masks*/\n")
	for line in peripheral.split():
		if line.find("<register>") != -1:
			registers = line
			found = 1
		elif line.find("</register>")!= -1:
			registers = registers + line
			struct_temp = ParseRegister(registers,peripheral_file,struct_temp)
			found = 0
		elif found == 1:
			registers = registers + line
	struct_temp = struct_temp+"}"+peripheral_name+"_;\n\n"
	peripheral_file.write("\n/*Defining a structure that holds all the "+peripheral_name+" registers*/")
	peripheral_file.write(struct_temp)
	peripheral_file.write("/*Defining the base adress for the " +peripheral_name+" and creating a struct at this base*/\n")
	peripheral_file.write("#define\t"+peripheral_name+"_BASE_ADDRESS\t\t"+peripheral_base)
	peripheral_file.write("\n#define\t"+peripheral_name+" (("+peripheral_name+"_ volatile * const)"+peripheral_name+"_BASE_ADDRESS)")
	return

def ParsePeripherals(user_file):
	xml_file = open(user_file,'r')
	xml_file.seek(0)
	found = 0
	peripherals = ""
	lines = xml_file.readlines()
	for line in lines:
		if line.find("<peripheral>") != -1:
			peripherals = line
			found = 1
		elif line.find("</peripheral>")!= -1:
			peripherals = peripherals + line
			ParsePeripheral(peripherals)
			found = 0
		elif found == 1:
			peripherals = peripherals + line			
	return

def XML_Parser():
	print("Welcome to the file parser v1.4")
	user_file = input("Please enter the file name  ")
	if path.exists(user_file):
		ParsePeripherals(user_file)
	else:
		print("<"+user_file +">"+" Wrong input: file doesn't exist")
	return 

if __name__ == '__main__':
	XML_Parser() 