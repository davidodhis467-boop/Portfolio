import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    print("=" * 40)
    print("       Email Validator Program")
    print("=" * 40)
    print("Type 'quit' to exit.\n")

    while True:
        email = input("Enter email address: ").strip()

        if email.lower() == 'quit':
            print("Goodbye!")
            break

        if validate_email(email):
            print(f"✅ ACCEPTED — '{email}' is a valid email.\n")
        else:
            print(f"❌ REJECTED — '{email}' is not a valid email.\n")

if __name__ == "__main__":
    main()