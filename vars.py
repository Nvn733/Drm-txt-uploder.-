#мιтσ¢нσи∂яια
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29020892"))
API_HASH = environ.get("API_HASH", "15bfac43cfbeb3993c942ce2f11ec3f8")
BOT_TOKEN = environ.get("BOT_TOKEN", "8096675089:AAFBP7q9ripjNz8oKIEk7szXDRKDX-dq8Ko")

OWNER = int(environ.get("OWNER", "7068000043"))
CREDIT = environ.get("CREDIT", "мιтσ¢нσи∂яια 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7068000043').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7068000043').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
