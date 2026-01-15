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





def estimate_bruteforce_time(entropy_bits: float, guesses_per_second: int = 1_000_000_000) -> str:
    """
    Estimate brute-force time given entropy and attacker guess rate.
    Default: 1 billion guesses per second (modern GPUs).
    """

    if entropy_bits == 0:
        return "Instantly cracked"

    total_guesses = 2 ** entropy_bits
    seconds = total_guesses / guesses_per_second

    if seconds < 60:
        return "Less than a minute"
    elif seconds < 3600:
        return "Less than an hour"
    elif seconds < 86400:
        return "Less than a day"
    elif seconds < 31536000:
        return "Less than a year"
    else:
        years = seconds / 31536000
        return f"Approximately {int(years)} years"
