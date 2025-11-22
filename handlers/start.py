# ============================================================
# Forward Tag Remover Bot
# Author: learningbots79 (https://github.com/learningbots79) 
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant
from config import Config
from database.mongo import mongo_db

FORCE_SUB_CHANNELS = Config.FORCE_SUB_CHANNELS
BOT_USERNAME = Config.BOT_USERNAME
UPDATES_CHANNEL = Config.UPDATES_CHANNEL
DEV_USERNAME = Config.DEV_USERNAME

# ================================================================
# Check Force Sub
# ================================================================
async def check_force_sub(client, message):
    for channel in FORCE_SUB_CHANNELS:
        try:
            await client.get_chat_member(channel, message.from_user.id)
        except UserNotParticipant:
            btn = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{channel}")]]
            )
            await message.reply_text(
                f"⚠️ You must join @{channel} to use the bot.",
                reply_markup=btn
            )
            return False
    return True

def init(app):
    @app.on_message(filters.command("start"))
    async def start_handler(client, message):
        allowed = await check_force_sub(client, message)
        if not allowed:
            return

        await mongo_db.add_user(message.from_user.id)

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Channel",
                    url=f"https://t.me/{BOT_USERNAME}?startchannel=true"
                )
            ],
            [
                InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/{DEV_USERNAME}")
            ]
        ])
        
        text = (
            "👋 Welcome to Forward Tag Remover Bot!\n\n"
            "I'm your assistant for removing the “Forwarded from” tag in Telegram channels.\n\n"
            "🛠 How it works:\n\n"
            "🔹 Add me as an admin in your channel — I’ll automatically remove tags from forwarded posts.\n"
            "🔹 You can also send forwarded messages here — I will return them clean.\n"
        )

        await message.reply_text(text, reply_markup=keyboard)