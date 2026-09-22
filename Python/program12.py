# Program 12: Check whether a given number is divisible by both 3 and 6

def main():
    number = int(input("Enter a number: "))

    if number % 3 == 0 and number % 6 == 0:
        print(f"{number} is divisible by both 3 and 6.")
    else:
        print(f"{number} is not divisible by both 3 and 6.")


if __name__ == "__main__":
    main()
