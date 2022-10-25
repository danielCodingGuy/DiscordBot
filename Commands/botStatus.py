#Command that displays discord bot status
#author: danielCodingGuy
  
  async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await client.change_presence(status=discord.Status.idle, activity = discord.Game('Status'))
        
        #You can change the game into a stream by changing keyword Game in discord.Game part of the code
        #Examples:
        # activity = discord.Game(name="!help") <--Game
        # activity = discord.Streaming(name="!help", url="twitch_url_here") <--Stream
        # activity = discord.Activity(type=discord.ActivityType.listening, name="!help") <--Listening to whatever
        # activity = discord.Activity(type=discord.ActivityType.watching, name="!help") <--Watching whatever
     
