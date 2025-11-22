# ============================================================
# Forward Tag Remover Bot
# Author: learningbots79 (https://github.com/learningbots79) 
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config


class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(Config.MONGO_URI)
        self.db = self.client[Config.DB_NAME]
        self.users = self.db.get_collection("users")

    async def init(self):
        # Create unique index for user_id
        await self.users.create_index("user_id", unique=True)

    async def add_user(self, user_id: int):
        # FIX: correct dictionary syntax
        await self.users.update_one(
            {"user_id": user_id},
            {"$setOnInsert": {"user_id": user_id}},
            upsert=True
        )

    async def get_user(self, user_id: int):
        return await self.users.find_one({"user_id": user_id})

    def all_users(self):
        return self.users.find({})


mongo_db = MongoDB()
