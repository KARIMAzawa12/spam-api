# 📧 Smart Email Guardian – Spam & Phishing Detector

This project detects whether an email is **Spam**, **Phishing**, or **Safe** using a machine learning model and a Flask API. It also includes a Flutter mobile app and a simple CLI tool.

---

## 🚀 Features

- ✅ Analyze emails via API or CLI  
- 📱 Mobile app (Flutter) for real-time analysis  
- 🔒 Detects both Spam and Phishing content  
- 📊 Clean and well-documented structure  

---

## 🛠️ Technologies Used

- Python 3  
- Flask (API backend)  
- Flutter (Mobile frontend)  
- Requests (for CLI)  
- JSON (for data exchange)  

---

## 🧪 How to Run

### 1. Start the API

```bash
cd spam-api
python app.py
```

### 2. Run the CLI Tool

```bash
python cli_tool.py
```

> Enter the email text in your terminal when prompted.

### 3. Run the Flutter App

Open the `flutter_app/` folder in Android Studio or VS Code and run:

```bash
flutter run
```

---

## 📝 API Endpoint

### POST `/analyze`

**Request:**

```json
{
  "email_text": "Click here to verify your account now!"
}
```

**Response:**

```json
{
  "result": "Phishing Email"
}
```

Possible results:
- `"Phishing Email"`  
- `"Spam Email"`  
- `"Safe Email"`  

---

## 📂 Project Structure

```
spam-api/
├── app.py            # Flask API server code
├── cli_tool.py       # Simple terminal-based CLI tool
├── flutter_app/      # Flutter project (mobile frontend)
└── README.md         # Documentation file
```

---

## 📬 Contact

Created with ❤️ by [KARIMA](https://github.com/KARIMAzawa12)
