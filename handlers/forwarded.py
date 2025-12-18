# ============================================================
# Forward Tag Remover Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from database.mongo import mongo_db
import logging

logger = logging.getLogger(__name__)

FORCE_SUB_CHANNELS = Config.FORCE_SUB_CHANNELS

# ================================================================
# Resend Post
# ================================================================.
async def resend_without_forward(msg: Message):
    try:
        if msg.text:
            await msg.reply_text(msg.text)

        elif msg.photo:
            await msg.reply_photo(msg.photo.file_id, caption=msg.caption or "")

        elif msg.video:
            await msg.reply_video(msg.video.file_id, caption=msg.caption or "")

        elif msg.document:
            await msg.reply_document(msg.document.file_id, caption=msg.caption or "")

        elif msg.animation:
            await msg.reply_animation(msg.animation.file_id, caption=msg.caption or "")

        elif msg.audio:
            await msg.reply_audio(msg.audio.file_id, caption=msg.caption or "")

        elif msg.voice:
            await msg.reply_voice(msg.voice.file_id, caption=msg.caption or "")

        elif msg.sticker:
            await msg.reply_sticker(msg.sticker.file_id)

        else:
            await msg.reply_text("Unsupported message type.")

    except Exception as e:
        logger.error(f"Error in Resend Post function: {e}")
