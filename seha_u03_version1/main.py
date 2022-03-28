class guest_book:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
 
    def __str__(self):
        return self.name + " ," + self.occupation
 
 
def menu():
    print("-----------------------------------------------------------------")
    print("                                                                 ")
    print("\n 1. Add a name and occupation                                  ")
    print("\n 2. List all users                                             ")
    print("\n 3. Exit                                                       ")
    print("                                                                 ")
    print("-----------------------------------------------------------------")
 
 
lst = []
 
menu()
user_input = False
guests = []
 
 
def option1():
    global user_input
    while user_input == False:
        name = input("Your name: ")
        occupation = input("Your occupation: ")
        if(name != "" and occupation != ""):
            guest = guest_book(name, occupation)
            guests.append(guest)
            user_input = True
    print("Guest added.")
    user_input = False
 
 
def option2():
    for guest in guests:
        print("\nName: " + guest.name + " Occupation: " + guest.occupation)
 
 
while(True):
 
    user = int(input("Choose 1 of 2 options: "))
 
    if user == 1:
        option1()
        pass
    if user == 2:
        option2()
        pass