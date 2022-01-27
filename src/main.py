import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

from src.utils.print_t import print_t

load_dotenv()

# https://my.telegram.org/
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')

# @JsonDumpBot ('message' -> 'forward_from_chat' -> 'id')
CHANNEL_FROM = int(os.getenv('CHANNEL_FROM'))
CHANNEL_TO = int(os.getenv('CHANNEL_TO'))

client = TelegramClient('forwarder', TELEGRAM_API_ID, TELEGRAM_API_HASH)


# https://docs.telethon.dev/en/stable/modules/events.html#telethon.events.newmessage.NewMessage
@client.on(events.NewMessage(incoming=True, forwards=False, chats=[CHANNEL_FROM]))
async def handler(event):
    message = event.message
    # for more filter - https://docs.telethon.dev/en/stable/modules/custom.html#module-telethon.tl.custom.message

    await client.send_message(CHANNEL_TO, message)
    print_t(f'message (id: {message.id}) forwarded')


def start():
    client.start()
    print_t('forwarder started')
    client.run_until_disconnected()
