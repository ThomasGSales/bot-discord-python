import discord
from key import token
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')


@client.event
async def on_ready():
    print(f'{client.user} está online')


@client.event
async def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return

    if l_conteudo.startswith("oliver sorteia os time aq"):
        # Separa os nomes em uma lista, removendo os espaços extras
        nomes = [nome.strip() for nome in message.content[26:].split(',')]

        # Embaralha a lista de nomes
        random.shuffle(nomes)

        meio = len(nomes) // 2

        adicionou_par = False

        # Percorre a lista, adicionando o par de || ao nome na posição central
        for i in range(len(nomes)):
            if i == meio and not adicionou_par:
                nomes[i] = f'**|||||** {nomes[i]}'
                adicionou_par = True
            else:
                nomes[i] = f'{nomes[i]}'

        # Junta os nomes em uma string separada por vírgula
        resposta = ', '.join(nomes)

        # Envia a resposta de volta para o canal
        await message.channel.send(f'times embaralhados: {resposta}')

    # comando para dar play

    if l_conteudo.startswith("tentra"):
        if message.author.voice:
            canal = message.author.voice.channel
            await canal.connect()
        else:
            await message.channel.send("entre em um canal pro bot entrar")

    if l_conteudo.startswith("tsai"):
        if message.author.voice:
            canal = message.author.voice.channel
            await canal.disconnect()
        else:
            await message.channel.send("o bot não está em nenhum canal")



client.run(TOKEN)
