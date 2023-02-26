
class Home():

    print("WELCOME TO HOTEL")
    print("1) Booking")
    print("2) Rooms Info")
    print("3) Room Service(Menu Card)")
    print("4) Payment")
    print("5) Record")
    print("6) Exit")

    ch = int(input("->"))

    if ch == 1:
        print(" ")
        # Booking()

    elif ch == 2:
        print(" ")
        # Rooms_Info()

    elif ch == 3:
        print(" ")
        # restaurant()

    elif ch == 4:
        print(" ")
        # Payment()

    elif ch == 5:
        print(" ")
        # Record()

    else:
        exit()

Home()
