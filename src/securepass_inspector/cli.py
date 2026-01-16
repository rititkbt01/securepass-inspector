import argparse
from securepass_inspector.checker.scorer import score_password


def main():
    parser = argparse.ArgumentParser(
        description="SecurePass Inspector - Password Security Analysis Tool"
    )

    parser.add_argument("password", type=str, help="Password to analyze")
    args = parser.parse_args()

    result = score_password(args.password)

    print("\n🔐 SecurePass Inspector Report")
    print("-" * 40)
    print(f"Risk Level : {result['risk']}")
    print(f"Score      : {result['score']} / 100")
    print(f"Entropy    : {result['entropy']} bits")
    print(f"Brute-force time (offline attack): {result['bruteforce_time']}")

    if result["issues"]:
        print("\n⚠️ Issues Found:")
        for issue in result["issues"]:
            print(f" - {issue}")
    else:
        print("\n✅ No major security issues detected.")

    print("-" * 40)


if __name__ == "__main__":
    main()
