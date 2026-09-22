# Program 17: Check whether the input contains a valid salary range

def main():
    salary = float(input("Enter the monthly salary: "))

    if salary <= 10000:
        print("Salary between 0 - 10,000: 10% tax")
    elif salary <= 20000:
        print("Salary between 10,001 - 20,000: 20% tax")
    elif salary <= 30000:
        print("Salary between 20,001 - 30,000: 30% tax")
    else:
        print("Salary above 30,000: 40% tax")


if __name__ == "__main__":
    main()
