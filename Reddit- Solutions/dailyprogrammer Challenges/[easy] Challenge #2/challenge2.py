
print("Newton's second law of motion describes the relationship between an object's mass and the amount of force needed to accelerate it.")

print("What would you like to calculate : ")
print("1. Force")
print("2. Mass")
print("3. Acceleration")

a = input("Choose an Option : ")

if a == 1:
	m = input("What is the Mass : ")
	acc = input("What is the Acceleration : ")
	print("Force = %d" %(m*acc))

elif a == 1:
	f = input("What is the Force : ")
	acc = input("What is the Acceleration : ")
	print("Force = %d"  %(f/acc))

elif a == 1:
	f = input("What is the Force : ")
	m = input("What is the Mass : ")
	print("Force = %d" %(f/m))	
