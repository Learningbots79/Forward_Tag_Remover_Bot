# ============================================================
# Forward Tag Remover Bot
# Author: learningbots79 (https://github.com/learningbots79)
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, PeerIdInvalid
from config import Config
from database.mongo import mongo_db
import logging
import asyncio

logger = logging.getLogger(__name__)
OWNER_ID = Config.OWNER_ID

# ================================================================
# INIT METHOD (REQUIRED FOR MAIN.PY)
# ================================================================
def init(app: Client):

    @app.on_message(filters.private & filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast_handler(client: Client, message: Message):
        if not message.reply_to_message:
            return await message.reply_text("Reply to a message to broadcast.")

        broadcast_message = message.reply_to_message
        success = 0
        failed = 0

        status = await message.reply_text("📢 Broadcast started...")

        async for user in mongo_db.all_users():
            user_id = user["user_id"]

            try:
                await broadcast_message.copy(chat_id=user_id)
                success += 1
                await asyncio.sleep(0.05)

            except FloodWait as e:
                await asyncio.sleep(e.value)

            except PeerIdInvalid:
                failed += 1

            except Exception as e:
                failed += 1
                logger.error(f"Error broadcasting to {user_id}: {e}")

        await status.edit_text(
            f"📢 Broadcast Completed\n"
            f"✅ Success: {success}\n"
            f"❌ Failed: {failed}"
        )
