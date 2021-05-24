readline_ = lambda x: f.readline().strip()
with open('credentials.txt', 'r') as f:
    account_sid = readline_(f)
    auth_token = readline_(f)
    from_ = readline_(f)
    to_ = readline_(f)
# print(account_sid, auth_token, from_, to)

from twilio.rest import Client

client = Client(account_sid, auth_token)

### SMS
message = client.messages.create(
    to=to_, 
    from_=from_,
    body="Hello from Mars!")
print(message.sid)
###

# from_whatsapp_number='whatsapp:' + from_
# to_whatsapp_number='whatsapp:+14155238886'# + to_

# client.messages.create(body='Hello from Planet Mars!',
#                        from_=from_whatsapp_number,
#                        to=to_whatsapp_number)