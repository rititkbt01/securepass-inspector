def check_basic_rules(password: str) -> dict:
    """
    Checks basic password security rules.
    """

    rules = {
        "min_length_12": len(password) >= 12,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special_char": any(not c.isalnum() for c in password),
    }

    return rules
