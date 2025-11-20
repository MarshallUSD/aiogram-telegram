from aiogram import Bot, Dispatcher, types
import asyncio
from token_api import TOKEN

bot = Bot(token=TOKEN)
dispatcher=Dispatcher(bot)


async def main():
    #entry point
    await dispatcher.start_polling()



if __name__ == "__main__":
    asyncio.run(main())


