#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="5001815038:AAGi1keQx-D22ZYKlgr2EMvdduIdYR6dYdM")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /audio
# отправляет заранее загруженное аудио по ID
@dp.message_handler(commands="audio")
async def cmd_test1(message: types.Message):
    await message.reply("Аудио-шмаудио")
    await message.reply_audio('CQACAgIAAxkBAAIBOGNEXVz0_xOhSxwOeScEojC2TkyQAALEHwACQDEoSuwQfFGhiTUGKgQ')

# отправляет аудио обратно и пишет его ID  чат
@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def echo_document(message: types.Message):
    await message.reply_audio(message.audio.file_id)
    await message.reply(message.audio.file_id)




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)