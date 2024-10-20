import discord
from discord.ext import commands
import random
import string
from discord.ext import commands
import asyncio

# Función para generar una contraseña aleatoria
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Función de adivinanza
def guess_number():
    return random.randint(1, 100)

# Lista de chistes
jokes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué el libro de matemáticas está estresado? Porque ya tenía demasiados problemas.",
    "Cual es el juego favorito de los musulmanes 😈. El jenga.",
    "¿Cuál es el pez más divertido? ¡El pez payaso!",
    "¿Por qué el policía no puede nadar? Porque tiene miedo de los ladrones de bancos."
]

# Lista de trivias
trivias = [
    "Los cocodrilos no pueden sacar la lengua.",
    "Las ranas pueden ver en todas las direcciones al mismo tiempo.",
    "El océano contiene suficiente sal para cubrir todos los continentes con una capa de 152 metros de espesor.",
    "El corazón de un camarón está en su cabeza.",
    "La miel nunca se echa a perder. Se han encontrado frascos con miel de más de 3000 años y aún era comestible.",
]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.command()
async def hello(ctx):
    await ctx.send(f"¡Hola, {ctx.author.name}!")

@client.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@client.command()
async def genpass(ctx):
    password = gen_pass(10)  # Llama a la función gen_pass
    await ctx.send(f'Tu nueva contraseña es: {password}')

@client.command()
async def roll(ctx):
    dice_roll = random.randint(1, 6)
    await ctx.send(f'Tiraste un dado y salió: {dice_roll}')

@client.command()
async def guess(ctx):
    target_number = guess_number()
    await ctx.send(f'He pensado en un número entre 1 y 100. ¡Adivina cuál es!')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        guess = await client.wait_for('message', check=check, timeout=30)
        if int(guess.content) == target_number:
            await ctx.send("¡Correcto! ¡Adivinaste el número!")
        else:
            await ctx.send(f"Incorrecto. El número era {target_number}.")
    except asyncio.TimeoutError:
        await ctx.send(f"Se acabó el tiempo. El número era {target_number}.")

@client.command()
async def joke(ctx):
    await ctx.send(random.choice(jokes))

@client.command()
async def trivia(ctx):
    await ctx.send(random.choice(trivias))

@client.command()
async def helpme(ctx):
    commands_list = """
    *Lista de Comandos:*
    - !hello: Saluda al bot.
    - !genpass: Genera una contraseña aleatoria.
    - !roll: Tira un dado de 6 caras.
    - !guess: Juego de adivinanza de número.
    - !joke: Cuenta un chiste.
    - !trivia: Te da una trivia interesante.
    - !play [url]: Reproduce música de YouTube en tu canal de voz.
    - !leave: Desconecta al bot del canal de voz.
    """
    await ctx.send(commands_list)

# Funciones para reproducir música con yt_dlp

ydl_opts = {
    'format': 'bestaudio',
    'noplaylist': 'True',
}

@client.command()
async def play(ctx, url: str):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()


@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Me he desconectado del canal de voz.")
    else:
        await ctx.send("No estoy en ningún canal de voz.")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)




bot.run('MTI4NzQxNjYwNjMxMzU0NTkwMA.GN3Sxv.ZbJArbyT6eLtQCYb1VdzzfY1F8HCtQ3IKUB0Zg')
