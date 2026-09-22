# Program 16: Check whether a 4-digit number is a narcissistic number or not

def main():
    number = int(input("Enter a 4-digit number: "))
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 4
        temp //= 10

    if total == number:
        print(f"{number} is a narcissistic number.")
    else:
        print(f"{number} is not a narcissistic number.")


if __name__ == "__main__":
    main()
