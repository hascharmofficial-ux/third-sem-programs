# Program 14: Take a number and print the square of each digit

def main():
    number = int(input("Enter a number: "))
    n = abs(number)

    print("Squares of digits:")
    while n > 0:
        digit = n % 10
        print(digit * digit)
        n //= 10


if __name__ == "__main__":
    main()
