backpack = ["matches", "flashlight", "energy bar"]
bckpck_max = 5

def help():             #prints available actions
        print("""\nAvailable Actions:
         E      Empty backpack
         L      Look in backpack
         C      Check backpack capacity
         A      Add an item to the backpack
         R      Remove an item from the backpack\
        """)

def action():         #executes actions from available action list  
        choice = input(": ")
        if choice.lower() == "help":
                help()
        elif choice.upper() == "E":
                empty_bckpck()
        elif choice.upper() == "L":
                look_bckpck()
        elif choice.upper() == "C":
                chck_bckpck_cap()
        elif choice.upper() == "A":
                add_bckpck()
        elif choice.upper() == "R":
                remove_bckpck()
        else:
                print("Not a valid choice")
        action()

                
def look_bckpck():              #prints a numbered list of the backpack's contents
        count = 0
        if len(backpack) == 0:
                print ("It's empty")
        else:
                for x in backpack:
                        count += 1
                        print (count, "     ", x)
                        
def chck_bckpck_cap():          #prints x/y where x is no of items in backpack and y is max capacity of backpack
        global backpack, bckpck_max
        print (len(backpack), "/", bckpck_max)
        
def add_bckpck():               #adds an item (a string) to the backpack
        global backpack      
        if len(backpack) < bckpck_max:
                item = input("What would you like to add? ")   
                backpack.append(item)
                print ("Added", item)
        else:
                print ("Sorry, your backpack is full. Do you want to swap an item out?")
                reply = input("Y/N:  ")
                if reply.upper() == "Y":
                        remove_bckpck()
                        add_bckpck()
                elif reply.upper() == "N":
                        action()
                else:
                        print ("You like to cause problems, don't you?")

def remove_bckpck():            #removes an item from the backpack
        global backpack
        look_bckpck()
        if len(backpack) == 0:
                print("There's nothing to remove!")
        else:
                item_num = int(input("Remove which item? \n:  "))
                try:
                        if item_num <= len(backpack) and item_num > 0:
                                print ("Removed", backpack[item_num - 1])
                                del backpack[item_num - 1]
                        else:
                                print ("Valid number pl0x")
                                remove_bckpck()
                except ValueError:
                        print("Enter the number slot of the item")
                        remove_bckpck()
      
def empty_bckpck():             #removes all items from backpack list
        global backpack
        backpack.clear()
        print ("Your backpack is now empty")



print ("Type 'help' to see list of available actions")
action()



