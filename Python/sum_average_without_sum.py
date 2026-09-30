# Lab Assignment - Question 2
# Problem: Take 10 integers from user, store in list, then find sum and average without sum().

def main():
    numbers = []
    print("Please enter 10 integers:")

    for i in range(1, 11):
        while True:
            try:
                num = int(input(f"Enter integer {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    # Calculate sum without using sum()
    total = 0
    for num in numbers:
        total += num

    # Calculate average
    average = total / len(numbers)

    print("\n--- Results ---")
    print("Stored List:", numbers)
    print("Sum of integers:", total)
    print(f"Average of integers: {average:.2f}")


if __name__ == "__main__":
    main()
