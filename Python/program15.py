# Program 15: Check whether a given number is an Armstrong number or not

def main():
    number = int(input("Enter a number: "))
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    if total == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")


if __name__ == "__main__":
    main()
