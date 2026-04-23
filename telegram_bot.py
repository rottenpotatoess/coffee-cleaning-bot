import pandas as pd
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import pytz
import os

TOKEN = os.getenv("8602149955:AAF3ZLoZMdp4GsmHckUp3yAmSf13sdbwEZE")
CHAT_ID = "1113145115"

bot = Bot(token=TOKEN)

def send_reminder():
    tz = pytz.timezone("Asia/Phnom_Penh")
    today = datetime.now(tz).strftime("%B %d, %Y").replace(" 0", " ")

    df = pd.read_excel("Coffee_Cleaning_Schedule_2026.xlsx")

    row = df[df["Date"] == today]

    if not row.empty:
        team = row.iloc[0]["Team"]
        members = row.iloc[0]["Assigned Members"]

        message = f"""
☕ ដល់ម៉ោងលាងកាហ្វេហើយបងៗ ☕
----Coffee Cleaning Reminder----

Date: {today}
Team: {team}
Assigned Members:
{members}

🙏សូមលាងម៉ាស៊ីនកាហ្វេផងណា🙏
🙏Please complete today's cleaning 🙏"""

        bot.send_message(chat_id=CHAT_ID, text=message)

scheduler = BlockingScheduler(timezone="Asia/Phnom_Penh")
scheduler.add_job(send_reminder, "cron", hour=16, minute=30)

print("Bot running...")
scheduler.start()