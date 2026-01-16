from .entropy import calculate_entropy
from .patterns import detect_patterns
from .bruteforce import estimate_bruteforce_time
from .hash_profiles import HASH_ATTACK_SPEEDS


def score_password(password: str, hash_type="bcrypt"):
    entropy = calculate_entropy(password)
    issues = detect_patterns(password)

    # 🔴 CRITICAL FIX: Penalize dictionary / human patterns
    if any("dictionary" in issue.lower() for issue in issues):
        entropy *= 0.4  # reduce entropy by 60%

    attack_speed = HASH_ATTACK_SPEEDS.get(hash_type, 1_000_000_000)
    bruteforce_time = estimate_bruteforce_time(entropy, attack_speed)

    score = 100

    if entropy < 40:
        score -= 40
    elif entropy < 60:
        score -= 20

    score -= len(issues) * 15
    score = max(score, 0)

    if score >= 80:
        risk = "Low"
    elif score >= 50:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "risk": risk,
        "score": score,
        "entropy": round(entropy, 2),
        "bruteforce_time": bruteforce_time,
        "issues": issues,
    }
