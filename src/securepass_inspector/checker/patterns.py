COMMON_PASSWORD_WORDS = [
    "password", "admin", "welcome", "login",
    "qwerty", "abc123", "letmein"
]

KEYBOARD_PATTERNS = [
    "qwerty", "asdf", "zxcv", "12345"
]


def detect_dictionary_words(password: str) -> bool:
    return any(word in password.lower() for word in COMMON_PASSWORD_WORDS)


def detect_keyboard_patterns(password: str) -> bool:
    return any(p in password.lower() for p in KEYBOARD_PATTERNS)


def detect_sequential_patterns(password: str) -> bool:
    sequences = ["0123", "1234", "2345", "abcd", "bcde", "cdef"]
    return any(seq in password.lower() for seq in sequences)


def detect_patterns(password: str):
    issues = []

    if detect_dictionary_words(password):
        issues.append("Contains common dictionary word")

    if detect_keyboard_patterns(password):
        issues.append("Contains keyboard pattern")

    if detect_sequential_patterns(password):
        issues.append("Contains sequential characters")

    return issues
