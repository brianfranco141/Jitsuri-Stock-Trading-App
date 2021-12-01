# For testing purposes I would recommend creating and registering for an alpaca paper trading account thats very easy to make and best of all free.
# Run this command to locally host server for the front layer and display

# connection for front end:
# server startup:  uvicorn main:app --reload

# Both the API_KEY and SECRET_KEY can be obtained through the alpaca trading platform 
API_KEY  = 
SECRET_KEY = 


# have the option to change to real/paper trading environment.
# paper tradin provides a way of testing with real world trading eviromnent as a way of back testing 
# https://paper-api.alpaca.markets or 'https:api.alpaca.markets
API_URL = 'https://paper-api.alpaca.markets'



# Make sure for the DB_FILE to app.db us linked with the directory of your cloned project

# EX: DB_FILE =  '/Users/brianfranco/Desktop/Developer/Projects/algorithmic-trading/Stock-Trading-App/app.db'
DB_File = 

# Can have the option to recieve tradding alerts via email and sms. More details on how to setup can be found here https://dev.to/mraza007/sending-sms-using-python-jkd
EMAIL_ADDRESS = 
EMAIL_SMS = 
EMAIL_PASSWORD = 
EMAIL_HOST = 
EMAIL_PORT = 
