# Lab Assignment - Question 3
# Problem: Input integers into a list and remove duplicates while preserving order.

def main():
    print("Enter integers separated by space:")
    raw_input = input("Integers: ").strip()

    if not raw_input:
        print("No input provided.")
        return

    # Parse integers from input
    try:
        numbers = [int(item) for item in raw_input.split()]
    except ValueError:
        print("Invalid input! Please enter only integers separated by space.")
        return

    print("Original list:", numbers)

    # Remove duplicates while preserving original order
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)

    print("List after removing duplicates (order preserved):", unique_numbers)


if __name__ == "__main__":
    main()
