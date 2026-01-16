import math

def calculate_entropy(password: str) -> float:
    """
    Calculate password entropy based on character pool size and length.
    Returns entropy in bits.
    """

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(not c.isalnum() for c in password):
        pool_size += 32  # Approximate special characters

    if pool_size == 0:
        return 0.0

    entropy = math.log2(pool_size ** len(password))
    return round(entropy, 2)
