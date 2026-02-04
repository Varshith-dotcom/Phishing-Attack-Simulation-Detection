phishing_keywords = ["login", "verify", "secure", "update", "account"]

url = input("Enter URL to analyze: ").lower()

if any(keyword in url for keyword in phishing_keywords):
    print("⚠️ Suspicious URL detected")
else:
    print("✅ URL looks safe (basic check)")
