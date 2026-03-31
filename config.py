from ast import pattern
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8040464811:AAHOVwkYCcehCnwFLcMtkZUaqSMEzGHLm_o")
BOT_USERNAME = 'KafkaX_Bot'
APP_ID = int(os.environ.get("APP_ID", "29245477"))
API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
OWNER_ID = int(os.environ.get("OWNER_ID", "8667251104"))
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URI", "mongodb+srv://Kafka:Au3OoWzCDYJKeuHU@cluster0.lz2m8iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cluster0")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
COMMAND_PHOTO = os.environ.get("COMMAND_PHOTO", "https://files.catbox.moe/hp9jnl.jpg")  # Replace with your photo URL
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/hp9jnl.jpg")
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/EternalsHelplineBot'>ᴏᴡɴᴇʀ</a></blockquote></b>")
ABOUT_TXT = os.environ.get("HELP_MESSAGE", "<b><blockquote>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ɪssᴜᴇs\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot</blockquote></b>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "<b><blockquote>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ɪssᴜᴇs.\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot</blockquote></b>")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://files.catbox.moe/hp9jnl.jpg")
FSUB_LINK_EXPIRY = 300
LOG_FILE_NAME = "CantarellaBots.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003746574484"))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
