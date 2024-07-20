import os.path

def add ():
    print("### ADD MODE ###")
    product = input("Product name: ")
    quantity = input("Quantity of product: ")
    price = input("Price of product: ")
    list = []
    with open("Files manager/sales_management.txt", "r") as f:
        content = f.readlines()
    for line in content:
        list += line.split(",")
    if product not in list:
        file_object = open("Files manager/sales_management.txt", 'a')
        file_object.write(f"{product}, {quantity}, {price}\n")
    else:
        print("the product is already on file")

def delete():
    product = input("What's the product you wanna delete ")
    deleted = False
    with open("Files manager/sales_management.txt", "r") as f:
        content = f.readlines()
    with open("Files manager/sales_management.txt", "w") as f:
        for line in content:
            if product not in line:
                f.write(line)
            else:
                print("The product was deleted")
                deleted = True
    if not deleted:
        print("You don't have the product in the file")
    
def consult():
    file_object = open("Files manager/sales_management.txt", 'r')
    print(file_object.read()) 

def update():
    print("### UPDATE MODE ###")
    print("Name|Quantity|Price")
    consult()
    product = input("What's the product name to update: ")
    list = []
    with open("Files manager/sales_management.txt", "r") as f:
        content = f.readlines()
    for line in content:
        list += line.split(",")
    if product in list:
        quantity = input("New quantity: ")
        price = input("New price: ")
        with open("Files manager/sales_management.txt", "w") as f:
            for line in content:
                if product  in line:
                    f.write(f"{product}, {quantity}, {price}")
                    print("the product was updated")
                else:
                    f.write(line)
    else:
        print("the product doesn't in the file")

def exit():
    os.remove("Files manager/sales_management.txt")
    open("Files manager/sales_management.txt", 'x')
    print("successful exit")
while True:
    action = input("add/delete a product or consult/update/exit the sales management file: ").lower()

    if action == "add":
        add()
    elif action == "delete":
        delete()
    elif action == "consult":
        consult()
    elif action == "update":
        update()
    elif action == "exit":
        exit()
        break
    else:
        print("invalid option")