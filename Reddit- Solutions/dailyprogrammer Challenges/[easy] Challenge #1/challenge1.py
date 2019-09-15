print("Please enter your Name, Age and Reddit Username")

#storing input for Name, Age and username
name = input("Name : ")
age = input("Age : ")
username = input("Reddit Username : ")

#printing the details
print ("Your name is " +name+ ", you are " +age+ " years old, and your Reddit Username is " +username)

#opening the text file and appending text
f = open("people_I_hacked.txt","a+")
f.write("\nYour name is " +name+ ", you are " +age+ " years old, and your Reddit Username is " +username)
f.close()
