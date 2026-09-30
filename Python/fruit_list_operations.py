# Lab Assignment - Question 1
# Problem: Create a list of 5 fruits, print 2nd and 4th items, replace last with "Mango", and print updated list.

def main():
    # 1. Create a list of 5 fruits
    fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    print("Original list of fruits:", fruits)

    # 2. Print 2nd and 4th items (index 1 and index 3 in 0-based indexing)
    print("2nd fruit (index 1):", fruits[1])
    print("4th fruit (index 3):", fruits[3])

    # 3. Replace the last item with "Mango"
    fruits[-1] = "Mango"

    # 4. Print the updated list
    print("Updated list of fruits:", fruits)


if __name__ == "__main__":
    main()
