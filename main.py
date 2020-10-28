from twilio.rest import Client
TWILIO_ACCOUNT_SID = "ACd330315b95a5f42f53b0bd3dc1b477af"
TWILIO_AUTH_TOKEN = "c9a7c305c103161ecda0acafd6eaedcf"

twilioClient = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+22890328783'
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():

    twilioClient.messages.create(body="dsds",
                                 from_=from_whatsapp_number,
                                 to=to_whatsapp_number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
