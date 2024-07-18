import os.path

master_pwd = input("What's the master password? ")
    
def master_pass():
    master = input("Write the master password: ")
    return master == master_pwd
def add():
    if master_pass():
        print("###ADD MODE###")
        
        username = input("Username: ")
        pwd = input("Password: ")
        file_object = open("passwords.txt", 'a')
        file_object.write('User: ')
        file_object.write(username)
        file_object.write(', Password: ')
        file_object.write(pwd + "\n")
    else:
        print("Incorrect password")
        master_pass()

def view():
    master = input("Write the master password: ")
    if master == master_pwd:
        print("###VIEW MODE###")
        file_object = open("passwords.txt", 'r')
        print(file_object.read()) 
while True:
    mode = input("Would you like to add a new password or view the passwords? (to exit press q) ").lower()
    """
    if os.path.isfile("passwords.txt"): #TO RESET THE FILE
        os.remove("passwords.txt")
        open("passwords.txt", 'x')
    """
    if mode == 'q':
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid option")