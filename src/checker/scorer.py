from src.checker.entropy import calculate_entropy
from src.checker.patterns import (
    detect_dictionary_words,
    detect_keyboard_patterns,
    detect_sequential_patterns
)
from src.checker.rules import check_basic_rules


def score_password(password: str) -> dict:
    """
    Calculates overall password risk score and classification.
    """

    score = 100
    reasons = []

    # 1. Basic rules
    rules = check_basic_rules(password)
    for rule, passed in rules.items():
        if not passed:
            score -= 10
            reasons.append(f"Failed rule: {rule}")

    # 2. Entropy evaluation
    entropy = calculate_entropy(password)
    if entropy < 50:
        score -= 30
        reasons.append("Low password entropy")

    # 3. Pattern detection
    if detect_dictionary_words(password):
        score -= 25
        reasons.append("Contains common dictionary word")

    if detect_keyboard_patterns(password):
        score -= 20
        reasons.append("Contains keyboard pattern")

    if detect_sequential_patterns(password):
        score -= 20
        reasons.append("Contains sequential pattern")

    # Normalize score
    score = max(score, 0)

    # Risk classification
    if score >= 80:
        risk = "LOW"
    elif score >= 50:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return {
        "score": score,
        "risk": risk,
        "entropy": entropy,
        "issues": reasons
    }
