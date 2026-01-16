# 🔐 SecurePass Inspector

SecurePass Inspector is a cybersecurity-focused CLI tool that analyzes password strength using **real attacker models**, not just math.  
It evaluates entropy, detects human patterns, estimates brute-force resistance, and assigns realistic risk levels.

This project was built **from scratch on Linux (WSL)** and reflects how real security teams evaluate password policies.

---

## 🎯 Problem Statement

Many “password strength checkers” are misleading.

They:
- Trust entropy math blindly
- Ignore dictionary attacks
- Mark passwords like `password123!` as “strong”

In reality, attackers **never brute-force these passwords** — they try them first.

**SecurePass Inspector fixes this.**

---

## 🛠️ Features

- ✅ Entropy calculation (character pool–based)
- ✅ Dictionary word detection
- ✅ Keyboard & sequential pattern detection
- ✅ Offline brute-force time estimation (GPU model)
- ✅ Risk scoring (Low / Medium / High)
- ✅ CLI interface (SOC-friendly)

---

## 🧠 How It Works (Security Logic)

1. **Entropy is calculated**
2. **Human patterns are detected**
3. **Entropy is penalized if patterns exist**
4. **Brute-force time is recalculated**
5. **Risk is assigned realistically**

> Entropy ≠ security  
> Human behavior matters more than math.

---

## ⚠️ Real Example

### Input
```bash
securepass-inspector "password123!"


### Output
Risk Level : High
Score      : 30 / 100
Entropy    : ~29 bits
Brute-force time (offline attack): seconds

Issues Found:
- Contains common dictionary word

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
