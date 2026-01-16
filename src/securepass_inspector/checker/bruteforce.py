def estimate_bruteforce_time(entropy_bits, guesses_per_second=1_000_000_000):
    total_guesses = 2 ** entropy_bits
    seconds = total_guesses / guesses_per_second

    if seconds < 60:
        return "seconds"
    elif seconds < 3600:
        return "minutes"
    elif seconds < 86400:
        return "hours"
    elif seconds < 31536000:
        return "days"
    else:
        years = seconds / 31536000
        return f"{int(years)} years"
