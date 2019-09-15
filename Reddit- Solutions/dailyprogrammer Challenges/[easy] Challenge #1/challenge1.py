print("Please enter your Name, Age and Reddit Username")

name = input("Name : ")
age = input("Age : ")
username = input("Reddit Username : ")


print ("Your name is " +name+ ", you are " +age+ " years old, and your Reddit Username is " +username)

f = open("test.txt","a+")

f.write("\nYour name is " +name+ ", you are " +age+ " years old, and your Reddit Username is " +username)
f.close()
