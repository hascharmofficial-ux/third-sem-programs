# Program 13: Accept temperature and humidity and print a message

def main():
    temperature = float(input("Enter temperature: "))
    humidity = float(input("Enter humidity: "))

    if temperature > 30 and humidity > 50:
        print("It is hot and humid.")
    else:
        print("Weather is normal.")


if __name__ == "__main__":
    main()
