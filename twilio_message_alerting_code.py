from twilio.rest import Client 
from flipkart_price_scraping import finalprice
account_sid = 'ACCOUNT_ID_OF_YOUR_TWILIO_ACCOUNT' 
auth_token = 'AUTH_TOKEN_OF_YOUR_TWILIO_ACCOUNT' 
client = Client(account_sid, auth_token) 
message = client.messages.create( 
							from_='whatsapp:YOUR_TWILIO_PHONE_NUMBER',  
							body=finalprice,      
							to='whatsapp:DESTINED_PHONE_NUMBER' 
							) 

print(message.sid)
