from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd0c4af2cce951c932c29c894e971249b"
auth_token  = "bb28e0ee955c0a1fa1d9c7ac1ad5124e"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Isn't this neat?",
    to="+15036168728",    # Replace with your phone number
    from_="+15412142359") # Replace with your Twilio number
print message.sid
