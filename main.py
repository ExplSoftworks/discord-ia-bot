import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

if not DISCORD_TOKEN or not OPENAI_API_KEY:
    raise SystemExit("Define DISCORD_TOKEN y OPENAI_API_KEY en las variables de entorno")

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True  # necesario para leer contenido de mensajes

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Bot conectado: {bot.user} (ID: {bot.user.id})")

@bot.command(name="ask", help="Haz una pregunta a la IA: !ask ¿Cuál es la capital de Francia?")
async def ask(ctx, *, question: str):
    await ctx.trigger_typing()
    try:
        resp = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": question}],
            max_tokens=600,
            temperature=0.7,
        )
        answer = resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        answer = "Error al consultar la API de IA: " + str(e)
    await ctx.reply(answer)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # responder cuando el bot sea mencionado
    if bot.user.mentioned_in(message):
        content = message.clean_content.replace(f"@{bot.user.name}", "").strip()
        if not content:
            content = "Hola"
        await message.channel.trigger_typing()
        try:
            resp = openai.ChatCompletion.create(
                model=MODEL,
                messages=[{"role": "user", "content": content}],
                max_tokens=600,
                temperature=0.7,
            )
            answer = resp["choices"][0]["message"]["content"].strip()
        except Exception as e:
            answer = "Error al consultar la API de IA: " + str(e)
        await message.reply(answer)

    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
