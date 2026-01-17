import random
import string


def generate_password(length: int, use_symbols: bool = True) -> str:
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$...

    charset = letters + digits
    if use_symbols:
        charset += symbols

    # Randomly pick characters from the allowed set
    return "".join(random.choice(charset) for _ in range(length))


def main():
    print("Password Generator")
    print("------------------")

    # Ask for length until the user enters a valid number
    while True:
        user_input = input("Password length (8-64): ").strip()
        if user_input.isdigit():
            length = int(user_input)
            if 8 <= length <= 64:
                break
        print("Please enter a number between 8 and 64.")

    symbols_input = input("Include symbols? (y/n): ").strip().lower()
    use_symbols = symbols_input in ("y", "yes")

    password = generate_password(length, use_symbols)
    print("\nGenerated password:")
    print(password)


if __name__ == "__main__":
    main()
