# Send WhatsApp Message via CLI with Twilio API

This script sends a WhatsApp message from your approved WhatsApp account to the customer number.

## Project Requirements

### Packages / Libraries
- `twilio`
- `dotenv`
- `os`

### Twilio Credentials 
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio authentication token
- `TWILIO_WHATSAPP_NUMBER`: Your WhatsApp number in the format `whatsapp:+13234560124`

### Approved Message
For example: "You have a new order"

## Running the Script
1. Run the command: `python notifyer.py`
2. You will be prompted to enter the customer's number.
3. After providing the number, you will receive a response on the status of the message.