import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlier import router



async def main():
    bot=Bot(token="8270373080:AAHjW2VLGKuekAe2N7SL3uorKskD0Hu51io")
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
       asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot toxtadi✅")   