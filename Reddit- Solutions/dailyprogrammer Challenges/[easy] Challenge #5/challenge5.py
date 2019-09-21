import time

def userValidator (username, password):
	userfile = open("username.txt")
	passfile = open("password.txt")
	realuser = userfile.readline()
	realpass = passfile.readline()
	print(realuser)
	print(realpass)
	if username == realuser and password == realpass:
		return 1
	return 0



username = input("Username : ")
password = input("Password : ")

if (userValidator (username, password)):
	print("User Validated.")
	time.sleep(3)
else:
	print("Incorrect Credentials. Exiting Program in 3 seconds.")
	time.sleep(3)
	exit(0)	


