from twilio.rest import Client

TWILIO_SID= "AC21f571e231bc3849cb530842fc056bcd"
TWILIO_AUTH_TOKEN= "44264239ad501f55dde106942eba2394"
TWILIO_NUMBER= "+12058807119"
MY_NUMBER= "+5583991157521"

class NotificationManager:
    def __init__(self):
        self.client= Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    
    def send_sms(self, message):
        message= self.client.messages.create(
            body= message,
            from_=TWILIO_NUMBER,
            to= MY_NUMBER
        )
        print(message.sid)
