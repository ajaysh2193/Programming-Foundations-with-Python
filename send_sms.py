from twilio.rest import Client

account_sid = "AC29cef0f17b8a58180dadf83d29aa713b"
auth_token = "4c9e7ef7588f3cf06fd662a022076eeb"
client = Client(account_sid, auth_token)

message = client.messages.create(to="+917531895977",
                                             from_="+17077556763",
                                             body="Hello there Ajay!")
print(message.sid)

