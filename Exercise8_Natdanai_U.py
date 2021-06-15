Username = input("Username")
Password = input("Password")

if Username == "1234" and Password == "5678":
    print("----------------------------------")
    print("Welcome to Ken Shop!")
    print("----------------------------------")
    print("Menu list")
    print("1.Banana 12 Baht")
    print("2.lay 20 Baht")
    print("3.Pad Kra Pao 50 Baht")
    print("4.Pad thai 50 Baht")
    print("5.Fanta 20 Baht")
    userSelected = int(input(">>"))
    if userSelected == 1:
        print("how much do you want?")
        result = 12*int(input())
        print("Price",result,"Baht")
    elif userSelected == 2:
        print("how much do you want?")
        result = 20 * int(input())
        print("Price",result,"Baht")
    elif userSelected == 3:
        print("how much do you want?")
        result = 50 * int(input())
        print("Price",result,"Baht")
    elif userSelected == 4:
        print("how much do you want?")
        result = 50 * int(input())
        print("Price",result,"Baht")
    elif userSelected == 5:
        print("how much do you want?")
        result = 20 * int(input())
        print("Price",result,"Baht")
else:
    print("Login failed")