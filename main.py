from aiogram import Bot, Dispatcher
import random
import asyncio
from datetime import datetime, timedelta
from time import sleep
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_TOKEN = os.environ.get('API_TOKEN')

bot_head = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot_head)
list_dobroutrov = ['Доброе утро', 'Доброго утречка', 'Боброе утро']
list_dobranichey = ['Спокойной ночи', 'Спокойно ночи', 'Споки ноки']

start_dobroutro = timedelta(hours=8)
start_dobranich = timedelta(hours=20)


def get_random_time(start):
    random_minutes = timedelta(minutes=random.randint(0, 59))
    return start + random_minutes


async def send_messages(start, msg: str, chat_id=int(os.environ.get('CHAT_ID'))):
    send_time = datetime.strptime(str(get_random_time(start)), '%H:%M:%S').time()
    while True:
        if f'{send_time:%H:%M}' == f'{datetime.now().time():%H:%M}':
            await bot_head.send_message(chat_id=chat_id, text=msg)
            break
        else:
            sleep(5)
    sleep(3700)


async def send_dobroutro():
    await send_messages(start_dobroutro, random.choice(list_dobroutrov))


async def send_dobranich():
    await send_messages(start_dobranich, random.choice(list_dobranichey))


async def main():
    while True:
        sleep(3700)
        await send_dobranich()
        sleep(3700)
        await send_dobroutro()
        sleep(3700)

if __name__ == '__main__':
    asyncio.run(main())
