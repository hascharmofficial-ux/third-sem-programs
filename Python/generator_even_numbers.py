# Program 24: Generator function to yield all even numbers up to a given limit

def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i


def main():
    print("Even numbers up to 10:")
    for num in even_numbers(10):
        print(num)


if __name__ == "__main__":
    main()
