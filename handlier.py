from aiogram.types import Message
from aiogram.filters import CommandStart, Command 
from aiogram import F, Router


router=Router()
dp=router


@dp.message(CommandStart())
async def cmd_start(message: Message):
      await message.answer("Qalay")
      await message.reply("Jumislaring qalay?")

@dp.message(Command("help"))
async def cmd_help(message: Message):
        await message.answer("Jardem kerekma?🤨")

@dp.message(F.text=="Hammesi jaqsi")
async def good(message: Message):
        await message.answer("Onda jaqsi😊")
