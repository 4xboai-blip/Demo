def check_even_odd(number):
    """Return 'Even' if number is even, otherwise 'Odd'."""
    return "Even" if number % 2 == 0 else "Odd"


def main():
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        return

    print(f"{number} is {check_even_odd(number)}")


if __name__ == "__main__":
    main()
