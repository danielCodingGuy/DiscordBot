#Command that can be used to kick member from the server if permission allows it
#Author: danielCodingGuy

@commands.has_permissions(kick_members=True)
if target.server_permissions.administrator:

    await bot.say("Target is an admin")

else:
    @bot.command()
    async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
            await user.kick(reason=reason)
            kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
            await ctx.message.delete()
            await ctx.channel.send(embed=kick)
            await user.send(embed=kick)

#This is early build, I haven't tested it properly yet so bear that in mind that it may not work great.
