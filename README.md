# gitman - ⚡️ GitHub Dorking URL Generator ⚡️

A tool for security researchers, penetration testers, and bug bounty hunters to identify potentially sensitive or exposed data within public GitHub repositories. This script leverages **GitHub dorking** techniques to help you find misconfigurations, exposed secrets, and vulnerable code that could pose a security risk.

> **Warning**: This tool is intended for **ethical hacking** and **security research** only. Always ensure you have explicit permission before testing any systems, and respect the terms of service for the platforms you are interacting with.
---

## 🚀 Quick Start 🚀

- **Installation**: [How to Install](#installation)
- **Usage**: [How to Use the Script](#usage)
- **Ethical Considerations**: [What You Need to Know](#ethical-considerations)
- **License**: [MIT License](#license)


## ⚙️ Table of Contents 🔍

- [🚀 Quick Start](#-quick-start)
- [💻 Features](#features)
- [🔍 Use Cases](#use-cases)
- [🛠 Installation](#installation)
- [💡 Usage](#usage)
- [📄 Input File Format](#input-file-format)
- [🔧 How It Works](#how-it-works)
- [⚖️ Ethical Considerations](#ethical-considerations)
- [📜 License](#license)
- [💬 Disclaimer](#disclaimer)

---


## ✨ Features ✨

- **Generate GitHub Search Queries**: The script allows you to create search URLs based on a company name and a set of dorking keywords (e.g., "password", "secret", "private", etc.).
- **Automated Search URL Generation**: For each keyword, the script generates a GitHub search URL that can quickly locate repositories with potential security risks.
- **Exclusion of False Positives**: Automatically filters out irrelevant results (e.g., "test", "example") to refine your search and focus on more valuable targets.
- **Command-Line Interface (CLI)**: Simple and flexible for integrating into penetration testing workflows or using in scripts for automation.

## 🛠️ Use Cases 🛠️

- **Reconnaissance for Penetration Testing**: Quickly identify sensitive information exposed on GitHub related to a specific target company or technology.
- **Bug Bounty Hunting**: Find exposed credentials, API keys, and other vulnerabilities in public repositories as part of a responsible bug bounty program.
- **Security Research**: Explore GitHub for potential security issues and public leaks, helping improve the overall security posture of organizations.

### 🎯 Example Targeting 🎯

- Search for publicly exposed API keys, database credentials, or other sensitive data.
- Investigate repositories related to specific companies or technologies to identify potential security flaws.
- Locate configuration files that may have been accidentally uploaded and are vulnerable to exploitation.

---
## 📋 Requirements 📋

- Python 3.x
- A text file containing dorking keywords (e.g., `github_dorking_keywords.txt`).

## 📦 Installation 📦

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sh1vam-03/gitman.git
   cd gitman
   ```

2. **No additional dependencies are required**, as the script uses only standard Python libraries.

## ⚙️ Usage ⚙️

The script accepts the company related keyword and an optional path to a custom file containing dorking keywords. You can use it like this:

### 🔑 Basic Usage (with default keyword file):

```bash
python gitman.py -k Google,Tesla
```

This will generate search URLs using the company name `Google` and `Tesla` with default `github_dorking_keywords.txt` file.

```bash
python gitman.py -k Google
```
```bash
python gitman.py -k Tesla
```

### 📂 Custom Keywords File:

If you have a custom list of dorking keywords (such as `api_key`, `password`, etc.), you can specify the file like this:

```bash
python gitman.py -k Google,Tesla -f custom_keywords.txt
```

### 🖥️ Example Output:

For each keyword in the file, the script generates a URL similar to:

```text
Generated GitHub Search URLs:
1 https://github.com/search?q=Google+"api_key"+NOT+test+NOT+example
2 https://github.com/search?q=Google+"api_key_secret"+NOT+test+NOT+example
3 https://github.com/search?q=Google+"api_key_sid"+NOT+test+NOT+example

1 https://github.com/search?q=Tesla+"api.googlemaps+AIza"+NOT+test+NOT+example
2 https://github.com/search?q=Tesla+"apidocs"+NOT+test+NOT+example
3 https://github.com/search?q=Tesla+"apikey"+NOT+test+NOT+example
...
```

These URLs direct you to GitHub search results that contain the target company name and the dorking keyword, excluding irrelevant entries like "test" or "example".

---

### 📃 Input File Format 📃

The input file should be a plain text file with one keyword per line. Empty lines or lines containing only whitespace will be ignored.

**Example (`github_dorking_keywords.txt`):**
```text
"API key"
"password"
"secret"
"confidential"
"access token"
"private key"
```

## 🧠 How It Works 🧠

- The script constructs GitHub search queries by appending the provided company related keywords and each keyword from the dorking file.
- It then generates search URLs like:
  ```
  https://github.com/search?q=Google+API+key+NOT+test+NOT+example
  ```
- The results filter out repositories related to "test" and "example" to help you focus on finding actual, potentially sensitive data.

## ⚖️ Ethical Considerations ⚖️

> **Important**: This tool is designed for **ethical hacking** purposes only. Before using it, ensure you have proper authorization to scan or interact with the target systems. Unauthorized scanning or data access could be illegal and violate GitHub's Terms of Service.

- **Penetration Testing**: Always conduct penetration testing only with explicit written permission from the target organization.
- **Bug Bounty**: If you’re using this tool for a bug bounty, ensure you're abiding by the program’s rules and guidelines.
- **Legal Use**: Never use this tool for malicious purposes or to exploit vulnerabilities without permission.

## ⚠️ Disclaimer ⚠️

This script is **not** intended for malicious activities. The creators of this script are not responsible for any misuse of the tool. By using this script, you agree to take full responsibility for your actions and ensure they comply with local laws and ethical standards.

## 🤖 License 🤖

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 🚨 Notes for Hackers 🚨

- **Customization**: You can modify the `load_dorking_keywords` function to load keywords from any other source (like a database or an API).
- **Security Considerations**: This script is intended to help identify exposed data. Always act responsibly and ensure that you do not inadvertently expose any data that could be sensitive or private.

