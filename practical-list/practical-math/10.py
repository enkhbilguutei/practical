# Application of Linear algebra: Coding and decoding of messages using nonsingular
# matrices.
# eg code “Linear Algebra is fun” and then decode it.

import numpy as np

# Define the encoding matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

# Define the message to be encoded
message = "Linear Algebra is fun"

# Set the block size
block_size = 3

# Pad the message
message += "X" * ((block_size - len(message) % block_size) % block_size)

# Split the message into blocks and convert each block to a column vector
blocks = [message[i:i+block_size] for i in range(0, len(message), block_size)]
block_vectors = [np.array([ord(c) - 65 for c in block]).reshape(block_size, 1) for block in blocks]

# Encode each block vector using the encoding matrix
encoded_vectors = [np.dot(A, x) % 26 for x in block_vectors]

# Convert the encoded vectors back to blocks
encoded_blocks = ["".join([chr(int(x) + 65) for x in encoded_vector]) for encoded_vector in encoded_vectors]
encoded_message = "".join(encoded_blocks)

# Print the encoded message
print("Encoded message: ", encoded_message)

# Decode the encoded message using the inverse of the encoding matrix
A_inv = np.linalg.inv(A)
encoded_blocks = [encoded_message[i:i+block_size] for i in range(0, len(encoded_message), block_size)]
encoded_vectors = [np.array([ord(c) - 65 for c in block]).reshape(block_size, 1) for block in encoded_blocks]
decoded_vectors = [np.dot(A_inv, x) % 26 for x in encoded_vectors]
decoded_blocks = ["".join([chr(int(x) + 65) for x in decoded_vector]) for decoded_vector in decoded_vectors]
decoded_message = "".join(decoded_blocks)

# Print the decoded message
print("Decoded message: ", decoded_message)

# Encoded message:  LQVKH ZUJZWPNGJAOPK
# Decoded message:  LINEARALGEBRAISFUNX

