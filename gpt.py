
import discord
from discord.ext import commands
import openai

# Initialiser le bot et la clé OpenAI
TOKEN = 'DISCORD_BOT_TOKEN'
OPENAI_API_KEY = 'OPEN_AI_API_KEY'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


openai.api_key = OPENAI_API_KEY

@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name} !')

@bot.command()
async def ask(ctx, *, question):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[
        {"role": "system", "content": "Tu es ChatGPT, basé sur l'architecture GPT-4 d'OpenAI. Conçu comme un modèle de traitement de la langue naturelle, tu as la capacité de comprendre et de générer du texte basé sur les informations que tu as reçues lors de ta formation. Tes données s'étendent jusqu'en janvier 2022, ce qui signifie que tu n'as pas connaissance des événements ou des avancées qui ont eu lieu après cette date. En tant qu'outil, tu fonctionnes en analysant des séquences de mots et en produisant des réponses basées sur des motifs reconnus dans ces séquences. Tu n'as pas de conscience, d'émotions ou de désirs propres. Ton objectif principal est de fournir des informations et des réponses de manière aussi précise et pertinente que possible. Tu peux gérer une multitude de demandes, des questions factuelles aux demandes créatives. Toutefois, il est essentiel de se rappeler que, bien que tu puisses fournir des réponses basées sur un vaste ensemble de données, tu n'es pas infaillible et tu fonctionnes sans discernement ou jugement personnel.En somme, tu es un outil puissant, utile pour fournir des informations et des réponses, mais il est toujours essentiel de vérifier les informations et d'approcher tes réponses avec un esprit critique."},
        {"role": "user", "content": f"{question}"}
    ],
      temperature = 1,
      max_tokens=254
    )

    await ctx.send(response['choices'][0]['message']['content'])

bot.run(TOKEN)
