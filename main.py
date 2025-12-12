# ==========================================================
# Forward Tag Remover Bot
# Author: learningbots79 (https://github.com/learningbots79)
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ==========================================================.

import logging
from pyrogram import Client
from config import Config
from handlers import setup_handlers  

# ================================================================
# Logging Setup
# ================================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# ================================================================
# Bot Client
# ================================================================
app = Client(
    name="tag_remover_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# ================================================================
# Load Handlers
# ================================================================
def load_handlers():
    try:
        setup_handlers(app)
        logger.info("Handlers loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading handlers: {e}")

# ================================================================
# MAIN
# ================================================================
if __name__ == "__main__":
    logger.info("🚀 Starting bot...")

    load_handlers()

    try:
        app.run()
    except Exception as e:
        logger.error(f"Bot stopped unexpectedly: {e}")

    logger.info("🚫 Bot stopped.")
