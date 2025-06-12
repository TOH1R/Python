import asyncio
from aiogram import Dispatcher, Bot
from app.handlers import dp

bot = Bot(token='7289182096:AAFG2ZlqaKzeG3y7FGPhRMxCjljMDbtCgkM')
router = Dispatcher(bot=bot)


async def main():
    router.include_router(dp)
    await router.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    