COMMON_PASSWORD_WORDS = [
    "password", "admin", "welcome", "login",
    "qwerty", "abc123", "letmein"
]

KEYBOARD_PATTERNS = [
    "qwerty", "asdf", "zxcv", "12345"
]

def detect_dictionary_words(password: str) -> bool:
    """
    Detects common dictionary words inside the password.
    """
    lower_pwd = password.lower()
    return any(word in lower_pwd for word in COMMON_PASSWORD_WORDS)


def detect_keyboard_patterns(password: str) -> bool:
    """
    Detects common keyboard patterns.
    """
    lower_pwd = password.lower()
    return any(pattern in lower_pwd for pattern in KEYBOARD_PATTERNS)


def detect_sequential_patterns(password: str) -> bool:
    """
    Detects sequential numeric or alphabetic patterns.
    """
    sequences = ["0123", "1234", "2345", "abcd", "bcde", "cdef"]
    lower_pwd = password.lower()
    return any(seq in lower_pwd for seq in sequences)
