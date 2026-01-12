#this program will take input from user and check the item n database f thats avalable it will be printed in output otherwise not available msg will be shared

user_input = input("please enter the name of item you wanna search :")

items = ['mouse','laptop','wire','water','book','phone','sound']

if user_input in items:
    print(f"the Item {user_input} is available")

else:
    print(f"this item {user_input} is not available")


    
