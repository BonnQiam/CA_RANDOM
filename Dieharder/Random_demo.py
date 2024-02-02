import random
import struct

num_numbers = 64000000
output_file = "random_numbers.bin"

with open(output_file, 'wb') as file:
    for _ in range(num_numbers):
        random_number = random.randint(0, 2**32 - 1)
        file.write(struct.pack('>I', random_number))  # Pack as 4-byte unsigned integer (32 bits)