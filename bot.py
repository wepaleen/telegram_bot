from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.utils.token import TokenValidationError
import asyncio
from scheduler import schedule_daily_quotes

# Токен твоего бота от BotFather
API_TOKEN = "7474934415:AAG8qNuQlaQJxEm2FyvfYE40je7FgSgHZtY"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Обработка команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Сәлам татар кызы!")
    # Запускаем отправку цитат каждый день
    schedule_daily_quotes(bot, message.from_user.id)

@dp.message(Command("regina"))
async def start_command(message: Message):
    await message.answer("😇 Регина, ты лучшая!😇")

async def main():
    try:
        await dp.start_polling(bot)
    except TokenValidationError:
        print("Неправильный токен бота. Проверьте его.")

if __name__ == "__main__":
    asyncio.run(main())
