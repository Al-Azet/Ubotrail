import asyncio
import os
from datetime import datetime
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from telethon.errors import (
    RPCError,
    ChannelPrivateError,
    ChannelInvalidError,
    MessageIdInvalidError,
    UserNotParticipantError
)
from fastapi import FastAPI
import re

# === KONFIGURASI ===
API_ID = 20958475
API_HASH = '1cfb28ef51c138a027786e43a27a8225'
SESSION = "1BVtsOLgBu4-pTf4jU1FVamzF-Srx68mNsX0Q0BgNHkRN8yIDYMTkNZRfMWyw-OJ-Mye0RtsOYhJNNOv_pbdyEilx5VoDH1dk6ib74mv0-6KKox48Gb7Ip5XzDHc-xqi2Bfi1Qe5IpjZ90tmsudTSNlq6fnYWa4YeXD7ywvHr_HQhoz-Ds1i8cofQx0R4dmdjNnk_oxrSVObSkYJRWM6HDPkP7iH79Jp7N9XpCxPOp52COTU0FuHa4wWTOqovf2ZCCgMoQcAtDIC0gGp3kMdkRayeYSm2e1SM2dMY7IXQQndhB4DdV9rjfLoQC7_9DYyMyzYk_PFTvGcbin9WhhceEm0-g6oBU44="
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# Fungsi untuk menangani event bot
async def start_bot():
    await client.start()
    print("Bot aktif.")

# === FastAPI untuk Endpoint HTTP ===
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Ubot aktif!"}

# Menjalankan bot di background
@app.on_event("startup")
async def on_startup():
    asyncio.create_task(start_bot())

# === Jalankan aplikasi ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
