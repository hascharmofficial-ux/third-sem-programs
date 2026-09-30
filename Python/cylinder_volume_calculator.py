# Program 11: Calculate the volume of a cylinder

def main():
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))

    pi = 3.14
    volume = pi * radius * radius * height
    print(f"Volume of cylinder: {volume}")


if __name__ == "__main__":
    main()
