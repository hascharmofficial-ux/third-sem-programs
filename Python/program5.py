# Lab Assignment - Question 5
# Problem: Input a list from user and reverse it without using reverse() or slicing.

def main():
    print("Enter elements of the list separated by space:")
    raw_input = input("Elements: ").strip()

    if not raw_input:
        print("Empty list entered.")
        return

    # Store elements in a list
    items = raw_input.split()

    print("Original list:", items)

    # Reverse without using reverse() or slicing
    # Using two-pointer in-place swap technique
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1

    print("Reversed list:", items)


if __name__ == "__main__":
    main()
