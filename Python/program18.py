# Program 18: Menu-driven unit conversion program

def main():
    print("Menu")
    print("1. Convert cm to inches")
    print("2. Convert km to miles")
    print("3. Convert USD to INR")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cm = float(input("Enter length in cm: "))
        inches = cm / 2.54
        print(f"{cm} cm = {inches} inches")
    elif choice == 2:
        km = float(input("Enter distance in km: "))
        miles = km * 0.621371
        print(f"{km} km = {miles} miles")
    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        inr = usd * 83
        print(f"{usd} USD = {inr} INR")
    elif choice == 4:
        print("Exiting the program...")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
