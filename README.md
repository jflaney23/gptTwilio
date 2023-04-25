# gptTwilio
A web app where the user can send a text to a Twilio number and then receive a ChatGPT response back via SMS.

# ChatGPT Twilio SMS Assistant

This is a simple Flask-based web application that integrates ChatGPT, an AI language model by OpenAI, with the Twilio SMS service. It allows users to interact with the ChatGPT assistant through SMS messages.

## Requirements

- Python 3.6+
- Flask
- Twilio
- OpenAI
- ngrok (for local testing)

## Installation

1. Clone this repository:
```
git clone https://github.com/jflaney23/gptTwilio.git
```

2. Change to the project directory:
```
cd chatgpt-twilio
```

3. Install the required packages using pip:
```
pip install -r requirements.txt
```

4. Set up your OpenAI API key as an environment variable:
```
export OPENAI_KEY=<your-openai-api-key>
```

5. Set up your Twilio account SID, auth token, and phone number as environment variables:
```
export TWILIO_ACCOUNT_SID=<your-twilio-account-sid>
export TWILIO_AUTH_TOKEN=<your-twilio-auth-token>
export TWILIO_PHONE_NUMBER=<your-twilio-phone-number>
```

## Usage

1. Start your Flask app:
```
python app.py
```

2. Start ngrok in a new terminal window to expose your local server to the public:
```
ngrok http 5000
```

3. Copy the HTTPS forwarding URL provided by ngrok (e.g., https://yoursubdomain.ngrok.io).

4. Configure your Twilio phone number's messaging webhook with the forwarding URL from ngrok. Append `/sms` to the URL (e.g., https://yoursubdomain.ngrok.io/sms).

5. Send an SMS to your Twilio phone number to interact with the ChatGPT assistant.
