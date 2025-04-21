from twilio.rest import Client
def sendmessage(ph,msg):
	# Your Account Sid and Auth Token from twilio.com / console
	account_sid = 'AC55a61b92f7dbb95daf4c4ef0f19780b3'
	auth_token = 'f9669ecc5c8a1fb9686cf9f8046d692a'

	client = Client(account_sid, auth_token)

	''' Change the value of 'from' with the number 
	received from Twilio and the value of 'to' 
	with the number in which you want to send message.'''
	message = client.messages.create(
								from_='+18126136296',
								body =msg,
								to ='+91'+ph
							)

	print(message.sid)

# sendmessage("9744734350","help me")