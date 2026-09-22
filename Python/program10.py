# Program 10: Calculate simple interest

def main():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time in years: "))

    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest: {simple_interest}")


if __name__ == "__main__":
    main()
