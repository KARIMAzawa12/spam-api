# # spam_detector.py

# def analyze_email(text):
#     phishing_keywords = ['verify', 'account', 'password', 'click here', 'urgent', 'login', 'bank']
#     spam_keywords = ['free', 'win', 'prize', 'offer', 'money', 'buy now']

#     text_lower = text.lower()

#     phishing_score = sum(word in text_lower for word in phishing_keywords)
#     spam_score = sum(word in text_lower for word in spam_keywords)

#     if phishing_score > 1:
#         return "Phishing Email"
#     elif spam_score > 1:
#         return "Spam Email"
#     else:
#         return "Safe Email"

# def main():
#     print("Enter your email text:")
#     email_text = input()
#     result = analyze_email(email_text)
#     print("Result:", result)

# if __name__ == "__main__":
#     main()
