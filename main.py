import discord

#early version, still in development
#author: danielCodingGuy

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$hello'):
            await message.reply('Hello!', mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')

#token can be stored in external .env file, will add it later down the line
