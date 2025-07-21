import requests
import json

def main():
    print("Welcome to the Email Analysis Tool (CLI Tool)")
    email_text = input("Enter the email text: ")

    url = "http://127.0.0.1:5001/analyze"  # Replace with your actual API address

    headers = {"Content-Type": "application/json"}
    data = {"email_text": email_text}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        print("\nAnalysis Result:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")

if __name__ == "__main__":
    main()
