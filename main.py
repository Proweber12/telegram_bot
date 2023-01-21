from aiogram import Bot, Dispatcher, types, executor
import random
import asyncio
from datetime import datetime, timedelta, time
from time import sleep
import os

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
            print(send_time)
            sleep(5)


async def send_dobroutro():
    await send_messages(start_dobroutro, random.choice(list_dobroutrov))


async def send_dobranich():
    await send_messages(start_dobranich, random.choice(list_dobranichey))


async def main():
    while True:
        await send_dobroutro()
        await send_dobranich()

if __name__ == '__main__':
    asyncio.run(main())
