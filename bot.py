import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from openai_gpt import text_complition

load_dotenv()


app = Client(
    "chatgpt-session",
    api_id=os.getenv("TG_API_ID"),
    api_hash=os.getenv("TG_API_HASH"),
    bot_token=os.getenv("BOT_TOKEN"),
)


@app.on_message()
async def echo(client, message):
    msg = message.text
    if msg == "/start":
        await app.send_message(message.chat.id,"Hello, This is a chatbot based on GPT-3.")
    else:
        res = text_complition(msg)
        if res["status"] == 1:
            await app.send_message(message.chat.id, res["response"])
        else:
            await app.send_message(message.chat.id,"Please try again later.")

            

app.run()
