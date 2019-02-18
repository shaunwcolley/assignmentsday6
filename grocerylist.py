#class MasterList:
#    def __init__(self):
#        self.lists = []


master_list = []

class GroceryItem:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

class ShoppingList:
    def __init__(self, list_name, description):
        self.list_name = list_name
        self.description = description
        self.items = []

    def show_item():
        for i in range(0, len(self.items)):
            print(f"{i + 1} {self.items[i].item_name}")

def add_list():
    list = ShoppingList(input("Please enter name of list:\n>> "), input("Please describe list:\n>> "))
    #print(f"{list.list_name}: {list.description}")
    master_list.append(list)

def show_lists():
    for i in range(0, len(master_list)):
        print(f"{i + 1} {master_list[i].list_name}")

def view_all_lists():
    for i in range(0, len(master_list)):
        print(f"{master_list[i].list_name} - {master_list[i].description}")
        for item in master_list[i].items:
            print(f"{item.item_name} - {item.quantity}")

def add_item():
    a = True
    while a == True:
        show_lists()
        list_add = int(input("Please enter list number:\n>> "))
        #for i in range(0, len(master_list)):
        if list_add - 1 not in range(0, len(master_list)):
            print("Please enter appropriate list number.")
        else:
            item = GroceryItem(input("Item name:\n>> "), input("How many:\n>> "))
            master_list[list_add - 1].items.append(item)
            #print(f"{master_list[list_add - 1].items}")
            print(f"{item.quantity} {item.item_name} added to {master_list[list_add - 1].list_name}")
            a = False

def del_list():
    show_lists()
    a = True
    while a == True:
        list_del = int(input("Please enter list number:\n>> "))
        if list_del <= len(master_list):
            del master_list[(list_del - 1)]
            a = False
        else:
            print(f"Please give a number up to {str(len(master_list) + 1)}, thank you!")
#not finished with del_item
def del_item():
    show_lists()
#    a = True
#    while a == True:
#        item_list = int(input("Please enter list number:\n>> "))
#        for i in range(0, len(master_list)):
#            if item_list - 1 == master_list[i]:
#                item_del = int(input("Please enter item number:\n>> "))
#                for i2 in range(0, len(master_list[i].items)):
#                    if item_del - 1 == master_list[i].items[i2]:
#                        del master_list[i].items[item_del-1]
#                        a == False
#                    else:
#                        print(f"Please give a number up to {str(len(master_list[i].items))}.")
#            else:
#                print(f"Please give a number up to {str(len(master_list) + 1)}, thank you!")

def show_menu():
    print("Please enter the following:")
    print("1 to create a new list")
    print("2 to add new item to list")
    print("3 to delete item")
    print("4 to delete list")
    print("5 to view all lists")
    print("q to quit")

user_input = ""
while user_input != "q":
    show_menu()
    user_input = input(">> ")
    if user_input == "1":
        add_list()
    elif user_input == "2":
        add_item()
    elif user_input == "3":
        del_item()
    elif user_input == "4":
        del_list()
    elif user_input == "5":
        view_all_lists()
    elif user_input != "q":
        print("Please Enter Valid Input")
