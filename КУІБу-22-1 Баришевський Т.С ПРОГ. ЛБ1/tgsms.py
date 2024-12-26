from telethon import TelegramClient

api_id = 'api_id'  
api_hash = 'api_hash_id' 
phone = 'nomer'

client = TelegramClient('session_name', api_id, api_hash)
async def send_message_to_user_or_chat(target, message):
    await client.start(phone=phone)
    try:
        await client.send_message(target, message)
        print(f"Відправленно: {message}")
    except Exception as e:
        print(f"Помилка: {e}")

async def main():
    target = 'chat_username або ссилка' 
    message = "Здарова! "
    
    await send_message_to_user_or_chat(target, message)

with client:
    client.loop.run_until_complete(main())
