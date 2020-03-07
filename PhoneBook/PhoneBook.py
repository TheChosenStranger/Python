import sys,os

def View(phonebook_view):
	phonebook_view.seek(0)
	user_input = input("Please choose (One, All): ")
	if user_input.lower() == "one":
		user_input = input("View by (ID, Name): ")
		temp_book = phonebook_view.readlines()
		if user_input.lower() == "id":
			user_id = input("Please Enter an ID  : ")
			if len(temp_book)<int(user_id) or int(user_id)==0:
				print("ID doesn't exist")
			else:
				print()
				print(temp_book[int(user_id)-1])
		elif user_input.lower() == "name":
			user_name = input("Please Enter a Name : ")
			temp_id = 0
			for lines in temp_book:
				temp_name = lines.split("-")[1]
				if temp_name.lower()==user_name.lower():
					temp_id = lines.split("-")[0]
					break
			if temp_id==0:
				print("Name doesn't exist")
			else:
				print()
				print(temp_book[int(temp_id)-1])
				print()
		else:
			print("<"+user_input +">"+" Wrong input: command not valid error code 0x4d6f7573746166612047686172656562 ")
	elif user_input.lower() == "all":
		print()
		for line in phonebook_view:
			print(line.rstrip("\n"))
		print()
	else:
		print("<"+user_input +">"+" Wrong input: command not valid error code 0x4d6f7573746166612047686172656562 ")
	return

def Add(phonebook_add):
	phonebook_add.readlines()
	if phonebook_add.tell() ==0:
		ID = 1
	else:
		phonebook_add.seek(0)
		for line in phonebook_add:
			temp = line.split("-")
			if len(temp)>0:	
				ID = int(temp[0])+1
	user_name = input("Please Enter Name  : ")
	user_number = input("Please Enter Number: ")
	user_mail = input("Please Enter E-mail: ")
	if user_name == "":
		user_name="N/A"
	if user_number == "":
		user_number="N/A"
	if user_mail == "":
		user_mail="N/A"
	phonebook_add.read()
	user_input = str(ID) + "-" + user_name + "-" + user_number + "-" + user_mail + "\n" 
	phonebook_add.write(user_input)
	return

def Remove(phonebook_remove):
	phonebook_remove.seek(0)
	exist = 0
	user_type = input("Remove by (ID, Name): ")
	if user_type.lower() == "id":
		user_id = input("Please Enter an ID  : ")
		temp_book = phonebook_remove.readlines()
		if len(temp_book)<int(user_id)  or int(user_id)==0:
			print("ID doesn't exist")
		else:
			del temp_book[int(user_id)-1]
			i = int(user_id)
			for lines in temp_book:
				temp_line = lines.split("-")
				if int(temp_line[0])> int(i):
					temp_line = str(i)+"-"+temp_line[1]+"-"+temp_line[2]+"-"+temp_line[3]
					temp_book[i-1] = temp_line
					i=i+1
			phonebook_remove.close()
			phonebook_remove = open("PhoneBook.txt",'w')
			for lines in temp_book:
				phonebook_remove.write(lines)
			phonebook_remove.close()
			phonebook_remove = open("PhoneBook.txt",'r+')
	elif user_type.lower() == "name":
		user_name = input("Please Enter a Name : ")
		temp_book = phonebook_remove.readlines()
		phonebook_remove.seek(0)
		temp_id = 0
		for lines in temp_book:
			temp_name = lines.split("-")[1]
			if temp_name.lower()==user_name.lower():
				temp_id = lines.split("-")[0]
				break
		if temp_id==0:
			print("Name doesn't exist")
		else:
			del temp_book[int(temp_id)-1]
			i = int(temp_id)
			for lines in temp_book:
				temp_line = lines.split("-")
				if int(temp_line[0])> int(i):
					temp_line = str(i)+"-"+temp_line[1]+"-"+temp_line[2]+"-"+temp_line[3]
					temp_book[i-1] = temp_line
					i=i+1
			phonebook_remove.close()
			phonebook_remove = open("PhoneBook.txt",'w')
			for lines in temp_book:
				phonebook_remove.write(lines)
			phonebook_remove.close()
			phonebook_remove = open("PhoneBook.txt",'r+')
	else:
		print("<"+user_input +">"+" Wrong input: command not valid error code 0x4d6f7573746166612047686172656562 ")
	return phonebook_remove

def PhoneBook():
	try:
		phonebook = open("PhoneBook.txt",'r+')
	except IOError:
		phonebook = open("PhoneBook.txt",'w')
		phonebook.close()
		print("**PhoneBook.txt was created and added to current directory**")
		phonebook = open("PhoneBook.txt",'r+')
	phonebook.seek(0)
	exit = 1;
	if len(sys.argv)==1:
		user_input = "NULL"
	else:
		user_input = sys.argv[1]

	while(exit):
		if user_input.lower() == "view":
			View(phonebook)
		elif user_input.lower() == "add":
			Add(phonebook)
		elif user_input.lower() == "remove":
			phonebook = Remove(phonebook)
		elif user_input.lower() == "":
			None
		else:
			print("<"+user_input +">"+" Wrong input: command not valid error code 0x4d6f7573746166612047686172656562 ")
		user_input = input("Please choose (View, Add, Remove, Exit): ")
		if user_input.lower() == "exit":
			exit = 0
			phonebook.close()
	return 

if __name__ == '__main__':
  PhoneBook() 