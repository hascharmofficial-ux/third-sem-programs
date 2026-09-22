# Program 8: Check whether three angles can form a valid triangle

def main():
    a = float(input("Enter angle 1: "))
    b = float(input("Enter angle 2: "))
    c = float(input("Enter angle 3: "))

    if a > 0 and b > 0 and c > 0 and (a + b + c) == 180:
        print("The angles can form a valid triangle.")
    else:
        print("The angles cannot form a valid triangle.")


if __name__ == "__main__":
    main()
