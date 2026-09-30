# Program 22: Decorator to double the result of any function

def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


@double_result
def add(a, b):
    return a + b


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add(a, b)
    print(f"Doubled sum: {result}")


if __name__ == "__main__":
    main()
