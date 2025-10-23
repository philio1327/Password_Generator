import string
import random

charset = string.ascii_letters + string.punctuation + string.digits

correct_input = False

while not correct_input:
    raw_input = input("Please input the length of your desired password (min 8): ")

    parsed = raw_input.strip()
    try:
        integer = int(parsed)
        if integer >= 8:
            correct_input = True
        else:
            print("Please enter a positive integer (minimum 8)!")
    except ValueError:
        print("Please enter a valid integer!")

password = "".join([random.choice(charset) for _ in range(integer)])
print(password)
