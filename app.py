from flask import Flask, request, jsonify

app = Flask(__name__)

def analyze_email(text):
    phishing_keywords = ['verify', 'account', 'password', 'click here', 'urgent', 'login', 'bank']
    spam_keywords = ['free', 'win', 'prize', 'offer', 'money', 'buy now']

    text_lower = text.lower()

    phishing_score = sum(word in text_lower for word in phishing_keywords)
    spam_score = sum(word in text_lower for word in spam_keywords)

    if phishing_score > 1:
        return "Phishing Email"
    elif spam_score > 1:
        return "Spam Email"
    else:
        return "Safe Email"

@app.route('/')
def home():
    return "API is running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'email_text' not in data:
        return jsonify({'error': 'Missing email_text'}), 400
    
    email_text = data['email_text']
    result = analyze_email(email_text)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
