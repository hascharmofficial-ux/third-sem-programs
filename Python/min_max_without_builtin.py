# Lab Assignment - Question 4
# Problem: Take 7 integers from user and find smallest and largest without min() or max().

def main():
    numbers = []
    print("Please enter 7 integers:")

    for i in range(1, 8):
        while True:
            try:
                num = int(input(f"Enter integer {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    # Find smallest and largest without using min() or max()
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print("\n--- Results ---")
    print("Entered numbers:", numbers)
    print("Smallest integer:", smallest)
    print("Largest integer:", largest)


if __name__ == "__main__":
    main()
