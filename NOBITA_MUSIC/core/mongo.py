from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import asyncio
import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://f7329984_db_user:bhaskarbaruah@cluster0.xjpwsjd.mongodb.net/?appName=Cluster0"

if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "No MONGO DB URL Found.. Your Bot Will Work On NOBITA MUSIC Database"
    )

    temp_client = Client(
        "NOBITA_MUSIC",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )

    async def client_info():
        await temp_client.start()
        info = await temp_client.get_me()
        await temp_client.stop()
        return info

    info = asyncio.get_event_loop().run_until_complete(client_info())
    username = info.username

    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)

    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]

else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)

    mongodb = _mongo_async_.Yukki
    pymongodb = _mongo_sync_.Yukki
