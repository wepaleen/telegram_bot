from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from quotes import get_random_quote

async def send_daily_quote(bot: Bot, user_id: int):
    quote = get_random_quote()
    await bot.send_message(user_id, quote)

def schedule_daily_quotes(bot: Bot, user_id: int):
    scheduler = AsyncIOScheduler()
    # Запуск каждые 5 минут
    scheduler.add_job(send_daily_quote, 'interval', minutes=1, args=[bot, user_id])
    scheduler.start()

