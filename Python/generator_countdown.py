# Program 23: Generator function to countdown from n down to 1

def countdown(n):
    while n >= 1:
        yield n
        n -= 1


def main():
    n = int(input("Enter starting number: "))
    print(f"Countdown from {n} down to 1:")
    for num in countdown(n):
        print(num)


if __name__ == "__main__":
    main()
