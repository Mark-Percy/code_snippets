import os
import base64

def generate_jwt_secret(length_bytes=32):
    """
    Generates a random secret key of specified byte length and encodes it in Base64.
    32 bytes = 256 bits (for HS256)
    64 bytes = 512 bits (for HS512, stronger)
    """
    if length_bytes < 32:
        print("Warning: For HS256, a secret key of at least 32 bytes (256 bits) is recommended.")
    
    # Generate random bytes
    random_bytes = os.urandom(length_bytes)
    
    # Encode to Base64
    base64_secret = base64.urlsafe_b64encode(random_bytes).decode('utf-8')
    
    return base64_secret

# Generate a 32-byte (256-bit) key for HS256
secret_hs256 = generate_jwt_secret(32)
print(f"\nGenerated 32-byte (HS256) Base64 Secret: {secret_hs256}")
print(f"Length (Base64 chars): {len(secret_hs256)}")

# Generate a 64-byte (512-bit) key for HS512 (stronger)
secret_hs512 = generate_jwt_secret(64)
print(f"\nGenerated 64-byte (HS512) Base64 Secret: {secret_hs512}")
print(f"Length (Base64 chars): {len(secret_hs512)}")

print("Ensure you keep this secret key confidential!")
