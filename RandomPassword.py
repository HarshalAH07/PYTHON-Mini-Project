import random
import string

pass_len = int(input("Enter Your Range: "))

values = string.ascii_letters + string.digits + string.punctuation

# List comprehension 

password = "".join([random.choice(values) for i in range(pass_len)])

print(password)