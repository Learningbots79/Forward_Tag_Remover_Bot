# ============================================================
# Forward Tag Remover Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================
from .start import init as start_init
from .broadcast import init as broadcast_handler_init
from .forwarded import resend_without_forward

def setup_handlers(app):

    start_init(app)
    broadcast_handler_init(app)
    resend_without_forward(app)