# Download the helper library from https://www.twilio.com/docs/python/install    
import os    
from dotenv import load_dotenv    
load_dotenv()    
                                                                                                           
from twilio.rest import Client    
    
          
# Find your Account SID and Auth Token at twilio.com/console    
# and set the environment variables. See http://twil.io/secure    
account_sid = os.getenv('TWILIO_ACCOUNT_SID')    
auth_token = os.getenv('TWILIO_AUTH_TOKEN')    
number_1 = os.getenv('NUMBER_1')
number_2 = os.getenv('NUMBER_2')

client = Client(account_sid, auth_token)   

call = client.calls.create(    
                       url='http://demo.twilio.com/docs/voice.xml',    
                       to=number_1,    
                       from_=number_2
                   )    
    
print(call.sid)
