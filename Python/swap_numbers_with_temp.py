# Program 19: Swap two numbers using a temporary variable

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    temp = a
    a = b
    b = temp

    print(f"After swapping: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
