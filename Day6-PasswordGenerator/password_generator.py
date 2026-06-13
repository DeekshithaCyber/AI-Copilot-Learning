import secrets
import string
print("=== password Generator ===")
length = int(input("Enter the lenght of the password:"))

characters = string.ascii_letters + string.digits+string.punctuation

password = ""
if length < 8:
    print("Password length should be at least 8 characters.")
else:
    for i in range(length):
        password += secrets.choice(characters)
    print("\n Generated password:",password)