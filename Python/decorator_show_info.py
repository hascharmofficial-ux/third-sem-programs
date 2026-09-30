# Program 21: Decorator to show execution info before and after function call

def show_info(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = func(*args, **kwargs)
        print("Function executed.")
        return result
    return wrapper


@show_info
def square(num):
    return num * num


def main():
    num = int(input("Enter a number: "))
    result = square(num)
    print(f"Square of {num}: {result}")


if __name__ == "__main__":
    main()
