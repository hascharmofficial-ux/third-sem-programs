# Program 7: Find the Euclidean distance between two points in 2D space

def main():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"The Euclidean distance is: {distance}")


if __name__ == "__main__":
    main()
