import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '2054877'))
API_HASH = environ.get('API_HASH', '4227c1e45e462209a3dcc67ada88a44f')
BOT_TOKEN = environ.get('BOT_TOKEN', '7499058839:AAHJ-zxAT8zT845ejdthVbg3nG5vavC1MKY')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '957158815').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/lovetoride')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001366123484'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://ltoride:ltoride@cluster0.c4ls2lb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://trvpn1:trvpn@cluster0.7kddrq3.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rahul")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rahul')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001366123484'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/wam.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002379152241').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001366123484'))
URL = environ.get('URL', 'https://switchle-auto3.zh4klt.easypanel.host/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001366123484'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/tgtamillinks/57")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/tgtamillinks/57")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/tgtamillinks/57")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://t.me/tgtamillinks/57")
SHORTENER_API = environ.get("SHORTENER_API", "5ef9638462736b0bf451579cd14d030da36f9f81")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "earnwithlink.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "5ef9638462736b0bf451579cd14d030da36f9f81")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "earnwithlink.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "5ef9638462736b0bf451579cd14d030da36f9f81")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "earnwithlink.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001366123484'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '4'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
