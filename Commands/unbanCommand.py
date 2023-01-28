#Command that can unban user that has been banned in the past
#author: danielCodingGuy

bot = Bot("$") #In this example you will need to use $ before command, use whatever you like in your bot.

@bot.command(name='unban')
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)

bot.run("token.env") #If you have your token in env file use it this way, if not you can pase your token there

#Gonna need these:  
#   from discord import User
#   from discord.ext.commands import Bot
