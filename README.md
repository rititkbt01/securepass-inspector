# 🔐 SecurePass Inspector

SecurePass Inspector is a **Python CLI tool** that analyzes password strength using entropy calculation, rule-based checks, and weak-pattern detection.

This project was built **from scratch as a beginner**, intentionally documenting real problems, debugging steps, and solutions encountered while building a cybersecurity tool the **professional way**.

---

## 📌 What This Project Does

- Evaluates password strength
- Detects weak or predictable patterns
- Calculates password entropy
- Provides clear security feedback via CLI

---

## 🎯 Why This Project Exists

Weak passwords are one of the most common causes of:
- Brute-force attacks
- Credential stuffing
- Account takeovers

This project demonstrates **how companies think about password security** and how such checks are implemented in real systems.

---

## 🏗️ Project Structure (Professional Layout)

```text
securepass-inspector/
├── src/
│   └── securepass_inspector/
│       ├── cli.py
│       └── checker/
│           ├── entropy.py
│           ├── rules.py
│           ├── patterns.py
│           ├── blacklist.py
│           └── scorer.py
├── pyproject.toml
├── .gitignore
├── README.md
