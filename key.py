import random
import string

def generate_key(length=25):
    """Generates a random key of the specified length, containing only letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Generate 150 keys, printing each on a new line
for _ in range(150):
    key = generate_key()
    print(key)
