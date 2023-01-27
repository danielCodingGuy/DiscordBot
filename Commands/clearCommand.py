#Command that can be used to delete messages from text channel
#Author: danielCodingGuy

@client.command()
@has_permissions(manage_messages = True)
async def clear(ctx , amount=5):
    await ctx.channel.purge(limit=amount + 1) #amount+1 to also delete the $clear shortly after writing it, if you dont want it simply set limit=amount

#Example: <!,*,- whatever you are using>clear <amount of messages>
#Make sure to give bot the permission to manage messages to avoid permission side problems with functionality
