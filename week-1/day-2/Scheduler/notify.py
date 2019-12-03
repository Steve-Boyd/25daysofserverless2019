from twilio.rest import Client
import json

with open('twilioconfig.json') as json_data_file:
        twilioconfig = json.load(json_data_file)


def main(msg):

    # account sid and auth token stored as env vars for easy access.
    account_sid = twilioconfig.account_sid
    auth_token = twilioconfig.auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            to=twilioconfig.to_number,
            from_=twilioconfig.from_number,
            body=msg)

    print(message.sid)
