#The whole thread about embed messages and how to do them in discord.py
#author: danielCodingGuy

#Core embed info - title, description, color
embed=discord.Embed(title="Embed example", url="https://github.com/danielCodingGuy", description="Lorem ipsum dolor", color=0xE6E6FA)

#Add more info to your embed, urls, icons
embed.set_author(name="danielCodingGuy", url="https://github.com/danielCodingGuy", icon_url="<yourIcon.com/icon.jpg>")

embed.set_thumbnail(url="<yourIcon.com/icon.jpg>")

#You can change the inline to make it appear one under another or one next to another
embed.add_field(name="Example Field 1", value="Lorem ipsum dolor sit amet 1", inline=False)
embed.add_field(name="Example Field 2", value="Lorem ipsum 2", inline=True)
embed.add_field(name="Example Field 3", value="Lorem ipsum 3", inline=True)

#Footer thingy if you want go ahead and use it
embed.set_footer(text="Footer Lorem ipsum dolor sit amet")

#Thats all on customizing embeds, if you want to send one do this
@client.event
async def on_message(message):
    if message.content.startswith('!embed'):
        embed=discord.Embed(title="Embed example", url="https://github.com/danielCodingGuy", description="Lorem ipsum dolor", color=0xE6E6FA)
        embed.set_author(name="danielCodingGuy", url="https://github.com/danielCodingGuy", icon_url="<yourIcon.com/icon.jpg>")
        embed.set_thumbnail(url="<yourIcon.com/icon.jpg>")
        embed.add_field(name="Example Field 1", value="Lorem ipsum dolor sit amet 1", inline=False)
        embed.add_field(name="Example Field 2", value="Lorem ipsum 2", inline=True)
        embed.add_field(name="Example Field 3", value="Lorem ipsum 3", inline=True)
        embed.set_footer(text="Footer Lorem ipsum dolor sit amet")
