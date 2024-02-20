import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

def send_whatsapp_message(to_number):
    
    message = "Hey, you have a new order on farmernear.me."

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=f'whatsapp:+91{to_number}'
        )
        print(f"Message sent to {to_number}. SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message to {to_number}: {str(e)}")

if __name__ == "__main__":
    to_number = input("Enter Farmer's Number (10digits): ")

    send_whatsapp_message(to_number)
