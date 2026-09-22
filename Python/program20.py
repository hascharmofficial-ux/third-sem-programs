# Program 20: Swap two numbers without using a temporary variable

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    a = a + b
    b = a - b
    a = a - b

    print(f"After swapping without temp: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
