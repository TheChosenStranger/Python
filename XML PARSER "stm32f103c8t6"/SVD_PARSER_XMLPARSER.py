import sys,os,re
from os import path
import xml.etree.ElementTree as ParseXML

def ParseField(field,peripheral_file):
	field_access = "write"
	for child in field.iter('field'):
			for counter in range(0,len(child)):
				if(child[counter].tag== 'name'):
					field_name =child[counter].text
					for counter2 in range(counter,len(child)):
						if child[counter2].tag == 'bitOffset':
							field_offset = child[counter2].text
							for counter3 in range(counter2,len(child)):
								if child[counter3].tag == 'bitWidth':
									field_width =child[counter3].text
									for counter4 in range(counter3,len(child)):
										if child[counter4].tag == 'access':
											field_access = child[counter4].text
			mask =  0
			for x in range(0,int(field_width)):
				mask =  mask +2**x
			mask = mask *2**(int(field_offset))
			mask = "0x%0.8X" % mask
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
	register_comm = "/**/"
	for child in register.iter('register'):
		for counter in range(0,len(child)):
			if(child[counter].tag== 'name'):
				register_name = child[counter].text
				for counter2 in range(counter,len(child)):
					if child[counter2].tag == 'description':
						register_comm = child[counter2].text
						for counter3 in range(counter2,len(child)):
							if child[counter3].tag == 'addressOffset':
								register_base = child[counter3].text
								for counter4 in range(counter3,len(child)):
									if child[counter4].tag == 'size':
										register_size = str(int(child[counter4].text,16))
		struct_temp = struct_temp +"\tu"+register_size+"\t"+register_name+";\t\t\t/*"+register_comm.splitlines()[0]+"*/\n"
		ParseField(child[counter],peripheral_file)
	return struct_temp

def ParsePeripheral(peripheral):
	struct_temp = ""
	for child in peripheral.iter('peripheral'):
		for counter in range(0,len(child)):
			if(child[counter].tag== 'name'):
				peripheral_name =child[counter].text
				peripheral_file = open(peripheral_name+"_register.h",'w')
				peripheral_file.write("/*This file was made by Moustafa Ghareeb*/\n")
				peripheral_file.write("/*Defining all main masks*/\n")
				struct_temp = "\ntypedef struct "+peripheral_name+"_\n{\n"
				for counter2 in range(counter,len(child)):
					if child[counter2].tag == 'baseAddress':
						peripheral_base = child[counter2].text
			struct_temp = ParseRegister(child[counter],peripheral_file,struct_temp)
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
	tree = ParseXML.parse(xml_file)
	root = tree.getroot()
	ParsePeripheral(root)
	return

def XML_Parser():
	print("Welcome to the file parser v1.6")
	user_file = input("Please enter the file name  ")
	if path.exists(user_file):
		ParsePeripherals(user_file)
	else:
		print("<"+user_file +">"+" Wrong input: file doesn't exist")
	return 

if __name__ == '__main__':
	XML_Parser() 